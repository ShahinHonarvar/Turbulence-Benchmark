import re
def insert_before_character(text):
    return re.sub(r'o', r'a\1', text)
