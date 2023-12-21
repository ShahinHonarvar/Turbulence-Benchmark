import re
def insert_before_character(text):
    return re.sub(r'(C)', r'H\1', text)
