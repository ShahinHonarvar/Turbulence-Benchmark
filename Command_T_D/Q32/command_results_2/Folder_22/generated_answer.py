import re
def insert_after_character(text):
    return re.sub(r'U', r'U\1', text)
