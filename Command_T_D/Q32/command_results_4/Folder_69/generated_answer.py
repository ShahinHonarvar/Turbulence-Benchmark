import re
def insert_after_character(text):
    return re.sub(r'(.)P', r'\1PP', text)
