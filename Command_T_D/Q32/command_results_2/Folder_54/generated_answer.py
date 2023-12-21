import re
def insert_after_character(string):
    return re.sub(r'(M)f', r'\1f', string)
