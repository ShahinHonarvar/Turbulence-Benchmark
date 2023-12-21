import re
def insert_before_character(text):
    return re.sub(r'(H)(?=\s)', r'\1s\2', text)
