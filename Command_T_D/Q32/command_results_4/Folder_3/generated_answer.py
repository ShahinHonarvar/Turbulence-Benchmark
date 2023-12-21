import re
def insert_after_character(s):
    return re.sub(r'0', r'0H', s)
