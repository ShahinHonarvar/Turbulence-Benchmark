import re
def insert_before_character(s):
    return re.sub(r'5', r'5\1', s)
