import re
def insert_after_character(text):
    return re.sub(r'(?<=t)u', 'u', text)
