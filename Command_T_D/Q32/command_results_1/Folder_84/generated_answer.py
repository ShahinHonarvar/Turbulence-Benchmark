import re
def insert_after_character(text):
    return re.sub(r'(H)(?=\s)', r'H\1n', text)
