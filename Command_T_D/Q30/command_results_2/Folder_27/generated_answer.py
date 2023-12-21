import re
def insert_before_character(s):
    return re.sub(r'(N)', r'j\1', s)
