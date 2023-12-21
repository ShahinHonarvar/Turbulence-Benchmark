import re
def insert_before_character(text):
    return re.sub(r'(?<=2)S', 'S', text)
