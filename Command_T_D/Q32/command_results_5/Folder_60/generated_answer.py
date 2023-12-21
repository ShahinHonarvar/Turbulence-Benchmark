import re
def insert_after_character(text):
    return re.sub(r'C(?!P)', r'CP', text)
