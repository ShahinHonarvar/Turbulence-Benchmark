import re
def insert_before_character(s):
    return re.sub(r'(?<=x)N', 'x', s)
