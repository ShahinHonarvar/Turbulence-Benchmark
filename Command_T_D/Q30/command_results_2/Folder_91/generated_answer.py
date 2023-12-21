import re
def insert_before_character(s):
    return re.sub(r'(a)', r'\1\0', s)
