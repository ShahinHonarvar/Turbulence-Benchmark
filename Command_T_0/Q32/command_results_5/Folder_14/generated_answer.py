import re
def insert_after_character(s):
    return re.sub(r'(.)\s', r'\1 \2', s)
