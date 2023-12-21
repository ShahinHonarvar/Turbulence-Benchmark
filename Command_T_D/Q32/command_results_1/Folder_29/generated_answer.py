import re
def insert_after_character(s):
    return re.sub(r'(N)z', r'\1zz', s)
