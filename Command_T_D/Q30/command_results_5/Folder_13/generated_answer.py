import re
def insert_before_character(text):
    return re.sub(r'x', r'N\x', text)
