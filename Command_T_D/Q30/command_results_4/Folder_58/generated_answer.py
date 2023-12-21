import re
def insert_before_character(s):
    return re.sub(r'(F)o', r'\1o', s)
