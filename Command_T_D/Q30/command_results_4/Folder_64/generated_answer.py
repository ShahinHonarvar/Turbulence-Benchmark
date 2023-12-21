import re
def insert_before_character(s):
    return re.sub(r'(u)', r'\1u', s)
