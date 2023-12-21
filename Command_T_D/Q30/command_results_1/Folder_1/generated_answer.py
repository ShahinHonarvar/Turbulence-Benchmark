import re
def insert_before_character(text):
    return re.sub(r'U', 'T\1', text)
