import re
def insert_after_character(s):
    return re.sub(r'(M)(?=.)', r'\1f', s)
