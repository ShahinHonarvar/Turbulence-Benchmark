import re
def insert_after_character(s):
    return re.sub(r'(?<=Y)4', r'4', s)
