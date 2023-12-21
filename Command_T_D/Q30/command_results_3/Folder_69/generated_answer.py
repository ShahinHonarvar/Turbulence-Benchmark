import re
def insert_before_character(s):
    return re.sub(r"(.*)P(.*)", r"\1P\2", s)
