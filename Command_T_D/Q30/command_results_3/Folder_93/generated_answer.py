import re
def insert_before_character(s):
    return re.sub(r'(?<=Y)4', r'4', s)
