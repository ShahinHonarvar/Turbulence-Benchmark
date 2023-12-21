import re
def insert_after_character(text):
    return re.sub(r'a(?!n)', r'an', text)
