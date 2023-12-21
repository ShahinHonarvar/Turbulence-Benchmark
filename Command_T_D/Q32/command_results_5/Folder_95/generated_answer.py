import re
def insert_after_character(s):
    return re.sub(r'(j)', r'\1q', s)
