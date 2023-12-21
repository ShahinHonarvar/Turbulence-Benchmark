import re
def insert_after_character(text):
    return re.sub(r'(?i)H(?!s)', r'H\1s', text)
