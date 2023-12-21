import re
def insert_before_character(text):
    return re.sub(r'(?<=A)H', r'H\1', text)
