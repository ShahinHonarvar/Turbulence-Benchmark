import re
def insert_after_character(s):
    return re.sub(r'(C)([A-Z])', r'\1H\2', s)
