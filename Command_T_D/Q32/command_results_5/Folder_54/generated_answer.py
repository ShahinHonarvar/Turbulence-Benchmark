import re
def insert_after_character(s):
    return re.sub(r"M(?!f)", "MF", s)
