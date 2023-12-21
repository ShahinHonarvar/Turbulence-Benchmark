import re
def insert_before_character(s):
    return re.sub(r'(6)', r'\1 9', s)
