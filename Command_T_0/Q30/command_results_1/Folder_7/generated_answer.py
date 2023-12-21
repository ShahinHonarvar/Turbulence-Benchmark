import re
def insert_before_character(s):
    return re.sub(r'(.)\s', r'\1H\s', s)
