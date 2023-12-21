import re
def insert_after_character(s):
    return re.sub(r'(E)', r'e\1', s)
