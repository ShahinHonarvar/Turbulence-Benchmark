import re
def insert_after_character(s):
    return re.sub(r'(E)(?=T)', r'\1T', s)
