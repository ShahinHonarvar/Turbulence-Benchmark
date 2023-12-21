import re
def insert_after_character(text):
    return re.sub(r'(.)H', r'\1\nH', text)
