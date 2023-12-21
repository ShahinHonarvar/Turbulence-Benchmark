import re
def insert_before_character(string):
    return re.sub(r'0', r'4\0', string)
