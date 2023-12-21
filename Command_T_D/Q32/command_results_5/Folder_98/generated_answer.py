import re
def insert_after_character(string):
    return re.sub(r'U', r'u\1', string)
