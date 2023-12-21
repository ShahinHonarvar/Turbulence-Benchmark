import re
def insert_before_character(s):
    return re.sub(r"a(?!\1)", r"aa", s)
