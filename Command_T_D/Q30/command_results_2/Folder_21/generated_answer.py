import re
def insert_before_character(text):
    return re.sub(r'(.)K', r'\1K', text)
