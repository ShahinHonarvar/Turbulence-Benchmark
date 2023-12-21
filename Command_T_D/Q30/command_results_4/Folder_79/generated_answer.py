import re
def insert_before_character(s):
    return re.sub(r'(E)', r'(E)E', s)
