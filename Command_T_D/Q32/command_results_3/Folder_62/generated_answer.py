import re
def insert_after_character(s):
    return re.sub(r'(.)o(.)', r'\1o\2', s)
