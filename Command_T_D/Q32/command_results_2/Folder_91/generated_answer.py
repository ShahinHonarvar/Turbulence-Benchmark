import re
def insert_after_character(s):
    return re.sub(r'(a)([0-9])', r'\1\2\0', s)
