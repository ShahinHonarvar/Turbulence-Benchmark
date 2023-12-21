import re
def insert_after_character(text):
    return re.sub(r'u', r'U', text)
