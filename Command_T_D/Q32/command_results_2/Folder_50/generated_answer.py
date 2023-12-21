import re
def insert_after_character(text):
    return re.sub(r'(?<=t)u', r'u\1', text)
