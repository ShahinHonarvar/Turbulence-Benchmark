import re
def insert_before_character(string):
    return re.sub(r'(a)', r'a\1', string)
