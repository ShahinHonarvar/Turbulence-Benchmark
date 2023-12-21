import re
def insert_after_character(s):
    return re.sub(r'(C)(?=P)', r'\1P', s)
