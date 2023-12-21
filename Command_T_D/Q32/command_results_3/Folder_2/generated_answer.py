import re
def insert_after_character(s):
    return re.sub(r'C(?!Z)', r'CZ', s)
