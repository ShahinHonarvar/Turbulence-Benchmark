import re
def insert_after_character(text):
    return re.sub(r'A(?!H)', r'AH', text)
