import re
def insert_before_character(text):
    return re.sub(r'(?<=\b)Y\b', r'4\b', text)
