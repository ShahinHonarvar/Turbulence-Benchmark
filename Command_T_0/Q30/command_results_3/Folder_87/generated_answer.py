import re
def insert_before_character(s):
    return re.sub(r'(?<=m)N', r'N', s)
