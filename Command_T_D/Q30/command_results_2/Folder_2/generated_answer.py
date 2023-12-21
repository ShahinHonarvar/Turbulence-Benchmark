import re
def insert_before_character(s):
    return re.sub(r'(C)', r'Z\1', s)
