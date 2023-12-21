import re
def insert_after_character(string):
    return re.sub(r'(?<=H)s', r'H\1s', string)
