import re
def insert_after_character(text):
    return re.sub(r'(?<=j)1', r'1', text)
