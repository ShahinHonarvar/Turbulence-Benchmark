import re
def insert_after_character(text):
    return re.sub(r'(.)\s', r'\1 \2', text)
