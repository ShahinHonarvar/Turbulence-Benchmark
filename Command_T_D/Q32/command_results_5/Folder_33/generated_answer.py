import re
def insert_after_character(s):
    return re.sub(r'(a)', r'\1n', s)
