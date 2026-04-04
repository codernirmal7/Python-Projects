import json

class MiniDB :
    """
    A simple in-memory database using list of dictionaries
    """

    def __init__(self , filename="data.json" , schema = []):
        self.filename = filename
        self.data = []
        self.schema = schema

    def load (self) :
        try :
            with open(self.filename , "r") as file :
                self.data = json.load(file)
        except FileNotFoundError :
            self.data = []
        

    def save (self) :
        """
        Save data to json file
        """
        with open(self.filename , "w") as file :
            json.dump(self.data , file, indent=4)
    
    def insert (self , record) :
        """
        Insert a new record (dictinoary)
        """
        if not self.schema_validation(record) :
            return False
        self.data.append(record)
        self.save()
        return True
    
    def select_all(self, limit=None, offset=0):
        """
        Return paginated records from self.data

        :param limit: Number of records to return (None = all)
        :param offset: Starting index
        """

        # Safety checks
        if offset < 0:
            raise ValueError("offset cannot be negative")

        if limit is not None and limit < 0:
            raise ValueError("limit cannot be negative")

        total_items = len(self.data)

        if offset >= total_items:
            return []

        # If no limit → return everything from offset
        if limit is None:
            return self.data[offset:]

        return self.data[offset: offset + limit]
    
    def select_where (self , user_input) :
        """
        Filter records by multiple conditions query
        """
        if not self.schema_validation(user_input) :
            return False
        results = []
        
        for record in self.data :
            if all(record[key] == value for key , value in user_input.items()) :
                results.append(record)

        return results
    
    def delete_where(self , key , value) :
        """
        Delete records matching condition
        """
        if not self.schema_key_validation(key) :
            print(f"{key} is not defined in schema")
            return False

        self.data = [
            record for record in self.data
            if not (key in record and str(record[key]) == value)
        ]

        self.save()
        return True

    def update (self , find , update_to) :
        """
        Update records by multiple conditons query 
        """
        if not self.schema_validation(find) or self.schema_validation(update_to) :
            return False

        update_count = 0
        for record in self.data :
            if all(record[key] == value for key , value in find.items()) :
                for key , value in update_to.items() :
                    record[key]=value
                update_count +=1
        
        self.save()
        return update_count
    

    def sort (self , key , is_reverse=False) :
        """
        Sorting by value wheather acessending or decending 
        """
        if not self.schema_key_validation(key) :
            print(f"{key} is not defined in schema")
            return False
        result = sorted(self.data , key=lambda x : x[key] , reverse=is_reverse)
        return result

    def generate_id(self):
        if not self.data:
            return 1
        return max(item.id for item in self.data) + 1
    
    def schema_validation (self , data) :
        for key , value in data.items() :
            if not self.schema_key_validation(key) :
                print(f"{key} is not defined in schema")
                return False
        return True
    
    def schema_key_validation (self , key) :
        return key in self.schema
