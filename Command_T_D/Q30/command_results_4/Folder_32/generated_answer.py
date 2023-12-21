import re
def insert_before_character(string):
    return re.sub(r'(F)', r'\1u', string)
