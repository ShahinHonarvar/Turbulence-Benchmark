import re
def insert_before_character(string):
    return re.sub(r'(?<=.)H', r'H\1', string)
