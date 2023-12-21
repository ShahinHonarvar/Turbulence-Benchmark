import re
def insert_before_character(string):
    return re.sub(r'(H)(?!s)', r'\1s', string)
