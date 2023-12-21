import re
def insert_after_character(text):
    return re.sub(r'4(?!F)', r'4F', text)
