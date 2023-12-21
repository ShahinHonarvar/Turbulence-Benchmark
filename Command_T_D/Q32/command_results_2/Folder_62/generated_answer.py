import re
def insert_after_character(string):
    return re.sub(r'(.)o(.)', r'\1o\2', string)
