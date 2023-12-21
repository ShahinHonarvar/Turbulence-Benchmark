import re
def insert_before_character(string):
    return re.sub(r'u', r'U\1', string)
