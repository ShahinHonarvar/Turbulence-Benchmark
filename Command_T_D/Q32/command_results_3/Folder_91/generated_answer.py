import re
def insert_after_character(string):
    return re.sub(r'a(?!0)', r'a0', string)
