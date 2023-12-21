import re
def insert_before_character(s):
    return re.sub(r'(?<=6)W', r'W\1', s)
