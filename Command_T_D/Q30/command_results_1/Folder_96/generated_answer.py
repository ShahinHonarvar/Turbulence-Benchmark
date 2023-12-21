import re
def insert_before_character(string):
    return re.sub(r'a', r'A\1', string)
