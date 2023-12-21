import re
def insert_before_character(text):
    return re.sub(r'(?<=r)1', '1', text)
