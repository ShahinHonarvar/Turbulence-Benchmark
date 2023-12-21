import re
def insert_before_character(string):
    return re.sub(r'(.)X', r'\1X', string)
