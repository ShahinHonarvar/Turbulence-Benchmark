import re
def insert_before_character(string):
    return re.sub(r'(V?)T', r'\1VT', string)
