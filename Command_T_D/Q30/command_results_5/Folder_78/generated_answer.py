import re
def insert_before_character(s):
    return re.sub(r'(H)(?=s)', r'\1s', s)
