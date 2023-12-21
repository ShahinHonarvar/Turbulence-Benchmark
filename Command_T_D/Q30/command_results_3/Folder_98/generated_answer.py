import re
def insert_before_character(string):
    return re.sub(r'U', r'u\1', string)
