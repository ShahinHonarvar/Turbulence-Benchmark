import re
def insert_before_character(text):
    return re.sub(r'j', r'1j', text)
