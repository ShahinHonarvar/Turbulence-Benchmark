import re
def insert_before_character(text):
    return re.sub(r'O', r'o\1', text)
