import re
def insert_before_character(text):
    return re.sub(r'(F)', r'\1o\1', text)
