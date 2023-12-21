import re
def insert_before_character(text):
    return re.sub(r'a(?!0)', r'0a', text)
