import re
def insert_before_character(text):
    return re.sub(r'X', r'\1\6', text)
