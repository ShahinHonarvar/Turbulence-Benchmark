import re
def insert_before_character(s):
    return re.sub(r'(?<=.)5', r'\1', s)
