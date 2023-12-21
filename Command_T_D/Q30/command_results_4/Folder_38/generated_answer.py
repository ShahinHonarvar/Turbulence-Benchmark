import re
def insert_before_character(text):
    return re.sub(r'(?<=X)6', '6', text)
