import re
def insert_before_character(string):
    return re.sub(r'F', r'u\1', string)
