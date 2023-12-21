import re
def insert_after_character(s):
    return re.sub(r"(.)K", r"\1\u203cK", s)
