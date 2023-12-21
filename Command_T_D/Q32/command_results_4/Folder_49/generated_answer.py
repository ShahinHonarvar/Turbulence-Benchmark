import re
def insert_after_character(text):
    return re.sub(r'(i)', r'i\1', text)
