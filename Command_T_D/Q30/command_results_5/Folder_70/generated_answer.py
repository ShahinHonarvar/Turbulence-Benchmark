import re
def insert_before_character(text):
    return re.sub(r'(P)', r'V\1', text)
