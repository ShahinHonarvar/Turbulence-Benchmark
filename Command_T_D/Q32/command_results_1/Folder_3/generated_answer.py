import re
def insert_after_character(text):
    return re.sub(r'0', r'0H', text)
