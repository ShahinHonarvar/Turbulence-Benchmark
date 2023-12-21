import re
def insert_after_character(s):
    return re.sub(r'(i)', r'\1I', s)
