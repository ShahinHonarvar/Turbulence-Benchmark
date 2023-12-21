import re
def insert_after_character(string):
    return re.sub(r'(j)', r'v\1', string)
