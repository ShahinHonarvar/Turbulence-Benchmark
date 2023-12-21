import re
def insert_after_character(s):
    return re.sub(r'b(?!y)', r'by', s)
