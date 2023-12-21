import re
def insert_before_character(s):
    return re.sub(r'(?<=X)6', '6', s)
