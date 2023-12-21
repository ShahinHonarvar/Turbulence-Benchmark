import re
def insert_before_character(s):
    return re.sub(r"t", r"G\1", s)
