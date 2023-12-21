import re
def insert_before_character(text):
    return re.sub(r'r', r'1r', text)
