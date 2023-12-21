import re
def insert_after_character(string):
    return re.sub(r'(u)', r'\1u', string)
