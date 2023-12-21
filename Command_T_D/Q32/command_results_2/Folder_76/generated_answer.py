import re
def insert_after_character(string):
    return re.sub(r'F', r'FM', string)
