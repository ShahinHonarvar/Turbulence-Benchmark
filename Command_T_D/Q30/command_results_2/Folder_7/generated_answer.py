import re
def insert_before_character(text):
    return re.sub(r'(.)H(.)', r'\1\1H\2', text)
