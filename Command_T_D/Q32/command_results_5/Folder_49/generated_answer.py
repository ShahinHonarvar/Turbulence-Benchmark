import re
def insert_after_character(s):
    return re.sub(r'(i)(?=i)', r'\1ii', s)
