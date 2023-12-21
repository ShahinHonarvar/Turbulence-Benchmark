import re
def insert_before_character(string):
    return re.sub(r'(j)', r'\1v', string)
