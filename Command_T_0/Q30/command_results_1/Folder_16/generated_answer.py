import re
def insert_before_character(s):
    return re.sub(r'(.)w', r'\1n\2', s)
