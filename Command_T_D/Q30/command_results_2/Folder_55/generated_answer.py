import re
def insert_before_character(text):
    return re.sub(r'u', r'U\1', text)
