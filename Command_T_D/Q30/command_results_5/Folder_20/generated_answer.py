import re
def insert_before_character(s):
    return re.sub(r'(C)', r'H\1', s)
