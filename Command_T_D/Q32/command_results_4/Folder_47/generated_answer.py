import re
def insert_after_character(text):
    return re.sub(r'(E)f', r'\1f', text)
