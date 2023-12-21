import re
def insert_before_character(text):
    return re.sub(r'9', r'\1M9', text)
