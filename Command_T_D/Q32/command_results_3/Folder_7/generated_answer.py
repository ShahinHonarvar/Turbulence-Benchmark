import re
def insert_after_character(string):
    return re.sub(r'(.)H', r'\1H\1', string)
