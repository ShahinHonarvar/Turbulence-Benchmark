import re
def insert_after_character(text):
    return re.sub(r'a\d', r'a0\d', text)
