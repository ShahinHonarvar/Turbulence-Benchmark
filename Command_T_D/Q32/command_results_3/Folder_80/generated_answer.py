import re
def insert_after_character(text):
    return re.sub(r'(.)X', r'\1XX', text)
