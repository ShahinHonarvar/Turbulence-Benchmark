import re
def insert_before_character(s):
    return re.sub(r'(Y)', r'\1 4', s)
