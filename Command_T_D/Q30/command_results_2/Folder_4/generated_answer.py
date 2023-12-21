import re
def insert_before_character(s):
    return re.sub(r'(?<=a)6', 'a6', s)
