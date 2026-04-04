import json
import re
from database import MiniDB


def parse_value(value: str):
    """
    Convert string to appropriate Python data type
    """

    value = value.strip()

    # Boolean
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False

    # None
    if value.lower() == "null":
        return None

    # Integer
    if value.isdigit():
        return int(value)

    # Float
    try:
        return float(value)
    except ValueError:
        pass

    # String (default)
    return value


def parse_input(user_input: str):
    """
    Convert input like:
    name=John age=18 active=true score=99.5
    into dictionary with correct types
    """

    parts = user_input.split()
    record = {}

    for part in parts:
        if "=" not in part:
            continue  # skip invalid parts

        key, value = part.split("=", 1)
        record[key] = parse_value(value)

    return record


def parse_select(command: str):
    """
    YOUR NEW QUERY PARSER
    Fully parses SQL-like SELECT queries:
    
    SELECT * 
    SELECT * WHERE age=18 AND name=John
    SELECT * WHERE age=18 AND name=John ORDER BY name DESC
    SELECT * LIMIT 10 OFFSET 5
    SELECT * WHERE age=18 ORDER BY age ASC LIMIT 10 OFFSET 2
    
    Returns a dict that the main loop can use directly with MiniDB.
    Supports AND conditions, ORDER BY, LIMIT, OFFSET.
    Case-insensitive for keywords (WHERE, AND, ORDER BY, LIMIT, OFFSET).
    """
    if not command.upper().startswith("SELECT"):
        return None

    cmd = command.strip()
    upper_cmd = cmd.upper()

    # Find keyword positions (case-insensitive)
    where_start = upper_cmd.find(" WHERE ")
    order_start = upper_cmd.find(" ORDER BY ")
    limit_start = upper_cmd.find(" LIMIT ")
    offset_start = upper_cmd.find(" OFFSET ")

    # Extract WHERE clause
    if where_start != -1:
        end_pos = min([p for p in [order_start, limit_start, offset_start] if p > where_start] or [len(cmd)])
        where_clause = cmd[where_start + len(" WHERE "):end_pos].strip()
    else:
        where_clause = None

    # Extract ORDER BY clause
    if order_start != -1:
        end_pos = min([p for p in [limit_start, offset_start] if p > order_start] or [len(cmd)])
        order_clause = cmd[order_start + len(" ORDER BY "):end_pos].strip()
    else:
        order_clause = None

    # Extract LIMIT clause
    if limit_start != -1:
        end_pos = min([p for p in [offset_start] if p > limit_start] or [len(cmd)])
        limit_clause = cmd[limit_start + len(" LIMIT "):end_pos].strip()
    else:
        limit_clause = None

    # Extract OFFSET clause
    if offset_start != -1:
        offset_clause = cmd[offset_start + len(" OFFSET "):].strip()
    else:
        offset_clause = None

    # Parse WHERE conditions (supports multiple AND)
    conditions = {}
    if where_clause:
        # Split on "AND" (case-insensitive, any whitespace)
        condition_strs = re.split(r'\s+AND\s+', where_clause, flags=re.IGNORECASE)
        for cond in condition_strs:
            cond = cond.strip()
            if "=" not in cond:
                continue
            key, val_str = [x.strip() for x in cond.split("=", 1)]
            conditions[key] = parse_value(val_str)

    # Parse ORDER BY
    sort_key = None
    sort_reverse = False
    if order_clause:
        order_parts = order_clause.split()
        if order_parts:
            sort_key = order_parts[0]
            if len(order_parts) > 1 and order_parts[1].upper() == "DESC":
                sort_reverse = True

    # Parse LIMIT
    limit = None
    if limit_clause:
        try:
            limit = int(limit_clause)
        except ValueError:
            limit = None

    # Parse OFFSET
    offset = 0
    if offset_clause:
        try:
            offset = int(offset_clause)
        except ValueError:
            offset = 0

    return {
        "where": conditions,
        "sort_key": sort_key,
        "sort_reverse": sort_reverse,
        "limit": limit,
        "offset": offset
    }


def main():
    db = MiniDB(schema=["id", "name", "age"])
    db.load()

    print("MiniDB with custom SQL-like query parser ready!")
    print("Try: SELECT * WHERE age=18 AND name=John")
    print("     SELECT * ORDER BY age DESC LIMIT 5")
    print("     SELECT * WHERE age=18 ORDER BY name ASC")

    while True:
        command = input("\n> ").strip()

        if command.startswith("insert"):
            data = command[len("insert "):]
            parsed = parse_input(data)
            parsed.pop("id", None)
            record = {"id": db.generate_id(), **parsed}
            response = db.insert(record)

            if not response:
                continue  

            print("Inserted!")

        # ==================== NEW QUERY PARSER BLOCK ====================
        elif command.upper().startswith("SELECT"):
            parsed_query = parse_select(command)
            if parsed_query is None:
                print("Invalid SELECT query format.")
                continue

            where_dict = parsed_query["where"]
            sort_key = parsed_query["sort_key"]
            sort_reverse = parsed_query["sort_reverse"]
            limit = parsed_query["limit"]
            offset = parsed_query["offset"]

            if where_dict:
                # Filter first
                results = db.select_where(where_dict)
                if results is False:
                    continue  # schema error already printed by MiniDB

                # Apply ORDER BY (on filtered results)
                if sort_key is not None:
                    if not db.schema_key_validation(sort_key):
                        print(f"{sort_key} is not defined in schema")
                        continue
                    results = sorted(results, key=lambda x: x[sort_key], reverse=sort_reverse)

                # Apply pagination (LIMIT / OFFSET)
                if offset >= len(results):
                    results = []
                elif limit is not None:
                    results = results[offset:offset + limit]
                else:
                    results = results[offset:]

            else:
                # No WHERE clause
                if sort_key is not None:
                    # Use existing db.sort (full table)
                    temp_results = db.sort(sort_key, sort_reverse)
                    if temp_results is False:
                        continue
                    results = temp_results

                    # Apply pagination
                    if offset >= len(results):
                        results = []
                    elif limit is not None:
                        results = results[offset:offset + limit]
                    else:
                        results = results[offset:]
                else:
                    # Simple select_all with pagination
                    results = db.select_all(limit=limit, offset=offset)

            # Print results (consistent with original select style)
            if not results:
                print("[]")
            else:
                for row in results:
                    print(row)

        elif command.startswith("delete "):
            condition = command[len("delete "):]
            key, value = condition.split("=")
            response = db.delete_where(key, value)
            if not response:
                continue
            print("Deleted!")

        elif command.startswith("update "):
            condition = command[len("update "):]
            data1, data2 = condition.split("set")

            find = parse_input(data1)
            update_to = parse_input(data2)

            response = db.update(find, update_to)
            if not response:
                continue
            print("Total updates count :", response)

        elif command == "exit":
            break

        else:
            print("Invalid command. Use SELECT ... or insert/delete/update/exit")


if __name__ == "__main__":
    main()
