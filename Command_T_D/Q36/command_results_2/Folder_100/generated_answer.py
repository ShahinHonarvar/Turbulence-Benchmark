 
import re
def filter_chars(str1):
    return re.sub(r'(?i)(?P<char>b[0-9]?)', '', str1)
