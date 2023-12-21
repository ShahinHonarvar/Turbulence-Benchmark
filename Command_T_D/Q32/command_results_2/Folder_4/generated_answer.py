import re
def insert_after_character(text):
    return re.sub(r'(?<=a)6', r'a6', text)
