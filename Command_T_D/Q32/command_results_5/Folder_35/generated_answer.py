import re
def insert_after_character(text):
    return re.sub(r'(?<=9)M', r'\1M', text)
