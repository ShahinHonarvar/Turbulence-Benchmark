import re
def insert_before_character(text):
    return re.sub(r'(.)H', r'\1H', text)
