import re
def insert_before_character(string):
    return re.sub(r'(?i)i', r'0\i', string)
