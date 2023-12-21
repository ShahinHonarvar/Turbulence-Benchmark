import re
def insert_before_character(text):
    return re.sub(r'U', r'F\1', text)
