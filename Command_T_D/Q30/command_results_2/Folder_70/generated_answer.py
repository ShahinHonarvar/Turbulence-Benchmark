import re
def insert_before_character(s):
    return re.sub(r'(P)', r'V\1', s)
