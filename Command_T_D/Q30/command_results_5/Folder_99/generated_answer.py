import re
def insert_before_character(s):
    return re.sub(r'(a)', r'W\1', s)
