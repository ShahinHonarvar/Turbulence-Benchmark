import re
def insert_before_character(string):
    return re.sub(r'(C)', r'P\1', string)
