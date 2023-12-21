import re
def insert_after_character(s):
    return re.sub(r'(.)H', r'\1HH', s)
