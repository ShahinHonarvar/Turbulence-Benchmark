import re
def insert_before_character(text):
    return re.sub(r'(Y)', r'\1\4', text)
