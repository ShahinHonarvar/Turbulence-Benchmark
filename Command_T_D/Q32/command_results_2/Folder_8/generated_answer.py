import re
def insert_after_character(string):
    return re.sub(r'(E)(?=T)', r'\1T', string)
