import re
def insert_before_character(s):
    return re.sub(r'(S)', r'U\1', s)
