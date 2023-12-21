import re
def insert_after_character(s):
    return re.sub(r'(H)([a-zA-Z])', r'\1s\2', s)
