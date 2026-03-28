import datetime
from enum import Enum


class LogEntry :
    """
    This class represents One log entry.

    Example log line:
    2026-03-09 10:31:04 ERROR Database connection failed
    """

    def __init__(self , timestamp  , level , message):
        self.timestamp = timestamp
        self.level = level
        self.message = message

class LogLevel(Enum):
    INFO = 1
    WARNING = 2
    ERROR = 3

class SortBy (Enum) :
    TIMESTAMP = 1
    LEVEL = 2

class LogAnalyzer :
    """
    Main class responsible for log reading and analyzing logs 
    """

    def __init__(self , filename):
        self.filename =  filename
        self.logs = []

    def load_logs (self) :
        """
        Read the log files and convert each line 
        into a LogEntry object.
        """
        with open(self.filename , "r") as file :
            for line in file :
                line = line.strip()

                if not line :
                    continue

                entry = self.parse_line(line)
                self.logs.append(entry)

    
    def parse_line (self , line) :
        """
        Convert a log line into a Entry object
        """

        parts = line.split(" ",3)
        if len(parts) < 4:
            return None

        date = parts[0]
        time = parts[1]
        level = LogLevel[parts[2]]
        message = parts[3]

        timestamp_str = f"{date} {time}"
        
        timestamp = datetime.datetime.strptime(timestamp_str , "%Y-%m-%d %H:%M:%S")

        return LogEntry(timestamp , level , message)
    
    def show_all_logs (self) :
        """
        Print all logs in formatted way
        """

        for log in self.logs :
            print(
                f"{log.timestamp} | {log.level} | {log.message}"
            )

    def count_log_levels (self) :
        """
        Count INFO / ERROR / WARNING 
        """

        counts = {}
        for log in self.logs :
            if log.level not in counts :
                counts[log.level] = 0
            
            counts[log.level] += 1

        return counts
    
    def export_report (self) :
        try :
            with open("logs_report.txt" , "w") as file :
                counts = self.count_log_levels()
                for level, count in counts.items():
                    file.write(f"{level} : {count}\n")
        except IOError as e :
            print("File already exist")
    
    
    def show_only_errors (self) :
        """
        This function only shows the errors
        """
        print("\n")
        for log in self.logs :
            if log.level == LogLevel.ERROR :
                self.print_log(log)

    def filter_by_date (self) :
        """
        Print the all logs from user entered date .
        """
        try :
            input_date = datetime.datetime.strptime(input("Enter date (eg. 2026-03-09) : "),"%Y-%m-%d")
            for log in self.logs:
                if log.timestamp.date() == input_date.date():
                    self.print_log(log)
        except ValueError:
            print("Something went worng")
    
    def search_logs (self) :
        """
        This function prints the searched keyword result , it print the those logs message keyword matching 
        with search text
        """
        print("Logs : ")
        self.show_all_logs()
        searched_keyword = input("Enter what you want to search : ").lower()
        print("\n")
        for log in self.logs :
            if searched_keyword in log.message.lower() :
                self.print_log(log)


    def sort_logs (self) :
        """
        This function sort by timestamp and level
        """
        for x in SortBy :
            print(f"{x.value} = {x.name}")

        sort_by = SortBy(int(input("Enter filter number: ")))
        sorted_logs = []

        if sort_by == SortBy.LEVEL :
            sorted_logs = sorted(self.logs , key=lambda x:  self.convert_log_level_to_number(x.level) , reverse=True)
        else :
            sorted_logs = sorted(self.logs , key=lambda x:  x.timestamp , reverse=True)
        
        for log in sorted_logs :
            self.print_log(log)
        

    # Helper function
    def print_log (self , log) :
        print(f"{log.timestamp} {log.level} {log.message}")

    def convert_log_level_to_number(self, level):
        return level.value
