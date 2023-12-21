import re
def insert_before_character(string):
    return re.sub(r'(?<=2)S', r'S\1', string)
