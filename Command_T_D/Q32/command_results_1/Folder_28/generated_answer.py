import re
def insert_after_character(text):
    return re.sub(r'r(?!1)', r'r1', text)
