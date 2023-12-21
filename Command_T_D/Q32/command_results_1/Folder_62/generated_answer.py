import re
def insert_after_character(s):
    return re.sub(r"((\s|^)o)", r"o\1", s)
