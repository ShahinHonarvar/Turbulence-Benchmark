import re
def insert_before_character(string):
    return re.sub(r'(s)', r'w\1', string)
