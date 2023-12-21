import re
def insert_before_character(s):
    return re.sub(r'(E)', r'\1T', s)
