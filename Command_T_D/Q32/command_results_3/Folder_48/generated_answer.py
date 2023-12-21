import re
def insert_after_character(s):
    return re.sub(r'S(?!U)', r'SU', s)
