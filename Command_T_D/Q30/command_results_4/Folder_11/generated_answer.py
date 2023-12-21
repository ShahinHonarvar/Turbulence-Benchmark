import re
def insert_before_character(text):
    return re.sub(r'(g)', r'\1t', text)
