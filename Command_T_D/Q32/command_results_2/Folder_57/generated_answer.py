import re
def insert_after_character(string):
    return re.sub(r'(s)', r'w\1', string)
