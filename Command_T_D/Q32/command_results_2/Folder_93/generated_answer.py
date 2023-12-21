import re
def insert_after_character(s):
    return re.sub(r'(.*?)Y', r'\1 4', s)
