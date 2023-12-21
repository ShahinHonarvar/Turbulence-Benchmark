import re
def insert_before_character(string):
    return re.sub(r'(C)', r'Z\1', string)
