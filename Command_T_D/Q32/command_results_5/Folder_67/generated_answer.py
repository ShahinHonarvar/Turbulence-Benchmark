import re
def insert_after_character(s):
    return re.sub(r"j(?!1)", r"1\1", s)
