import re
def insert_after_character(string):
    return re.sub(r'O', r'o\1', string)
