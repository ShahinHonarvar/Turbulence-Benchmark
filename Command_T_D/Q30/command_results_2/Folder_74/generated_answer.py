import re
def insert_before_character(s):
    return re.sub(r'(T)', r'\1 \2', s)
