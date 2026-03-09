import datetime
from enum import Enum

class Priority (Enum) :
    HIGH = 1
    MEDIUM = 2
    LOW = 3


class Filter (Enum) :
    COMPLETED = 1
    NOT_COMPLETED = 2
    HIGH_PRIORITY = 3

class Sorting(Enum) :
    PRIORITY = 1
    DUE_DATE = 2
    TITLE = 3

class Utilites :
    def __init__(self):
        pass

    def string_to_date(self,date_str, date_format="%Y-%m-%d"):
        """
        Convert a string to a datetime object.
        
        :param date_str: The date string to convert.
        :param date_format: The expected format of the date string (default: YYYY-MM-DD).
        :return: datetime object if successful, None if invalid.
        """
        try:
            # Attempt to parse the date string
            date_obj = datetime.datetime.strptime(date_str, date_format)
            return date_obj
        except ValueError as e:
            print(f"Error: {e}. Please use the format {date_format}.")
            return None
        
    def date_validation (self , date  ) :
        if not isinstance(date, datetime.datetime):
            return False
        else :
            return True
        
    
        
    
