import re
def insert_before_character(s):
    return re.sub(r'(i)', r'\1i', s)
