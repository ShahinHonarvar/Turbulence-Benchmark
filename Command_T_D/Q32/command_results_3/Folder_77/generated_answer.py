import re
def insert_after_character(s):
    return re.sub(r'(?<=9)h', 'h', s)
