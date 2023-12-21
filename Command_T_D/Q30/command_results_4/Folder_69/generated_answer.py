import re
def insert_before_character(text):
    return re.sub(r'(.)\sP', r'\1\sP', text)
