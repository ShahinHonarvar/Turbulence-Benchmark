import re
def insert_before_character(text):
    return re.sub(r'(E)(?=T)', r'\1T', text)
