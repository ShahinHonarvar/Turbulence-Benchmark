import re
def insert_after_character(string):
    return re.sub(r'(T)s', r'\1T \2s', string)
