import re
def insert_after_character(string):
    return re.sub(r'o', r'0\1', string)
