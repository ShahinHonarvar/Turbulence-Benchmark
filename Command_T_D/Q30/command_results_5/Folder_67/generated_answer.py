import re
def insert_before_character(s):
    return re.sub(r'(?<=j)1', '1', s)
