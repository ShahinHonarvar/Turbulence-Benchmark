import re
def insert_after_character(s):
    return re.sub(r"m(?!Q)", r"mQ", s)
