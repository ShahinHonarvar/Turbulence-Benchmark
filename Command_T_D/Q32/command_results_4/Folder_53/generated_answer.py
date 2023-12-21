import re
def insert_after_character(s):
    return re.sub(r'(i)(?=\bI)', r'\1I', s)
