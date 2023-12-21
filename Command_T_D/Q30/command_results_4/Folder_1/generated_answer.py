import re
def insert_before_character(string):
    return re.sub(r'U', 'T\1', string)
