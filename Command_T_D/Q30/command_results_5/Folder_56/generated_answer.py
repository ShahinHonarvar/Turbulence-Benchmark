import re
def insert_before_character(text):
    return re.sub(r'I', r'i\1', text)
