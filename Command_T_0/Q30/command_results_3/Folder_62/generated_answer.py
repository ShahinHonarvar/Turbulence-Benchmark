import re
def insert_before_character(s):
    return re.sub(r'(.)o', r'\1o', s)
