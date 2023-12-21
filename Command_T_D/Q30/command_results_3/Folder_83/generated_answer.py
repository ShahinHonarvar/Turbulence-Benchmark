import re
def insert_before_character(text):
    return re.sub(r'(E)', r'e\1', text)
