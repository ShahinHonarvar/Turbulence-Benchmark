import re
def insert_after_character(text):
    return re.sub(r'(?<=H)n', r'\1', text)
