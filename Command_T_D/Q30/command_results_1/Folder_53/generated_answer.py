import re
def insert_before_character(text):
    return re.sub(r'(i)', r'\1I', text)
