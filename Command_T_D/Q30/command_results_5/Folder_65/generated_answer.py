import re
def insert_before_character(string):
    return re.sub(r'6', r'9\6', string)
