import re
def insert_before_character(text):
    return re.sub(r'(C)', r'Z\1', text)
