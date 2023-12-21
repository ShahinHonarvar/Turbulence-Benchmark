import re
def insert_before_character(text):
    return re.sub(r'(?! )T', r'\1 \2', text)
