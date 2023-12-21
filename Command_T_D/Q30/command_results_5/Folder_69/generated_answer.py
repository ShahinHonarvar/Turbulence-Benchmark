import re
def insert_before_character(text):
    return re.sub(r'(.)\s', r'\1P\s', text)
