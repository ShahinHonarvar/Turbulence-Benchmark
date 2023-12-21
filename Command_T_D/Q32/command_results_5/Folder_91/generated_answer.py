import re
def insert_after_character(string):
    return re.sub(r'a', r'0\1', string)
