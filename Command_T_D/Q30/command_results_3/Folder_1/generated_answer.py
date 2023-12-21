import re
def insert_before_character(string):
    return re.sub(r'U', r'T\1', string)
