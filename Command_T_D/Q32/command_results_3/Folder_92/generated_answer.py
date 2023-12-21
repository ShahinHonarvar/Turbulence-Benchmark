import re
def insert_after_character(text):
    return re.sub(r'(a)', r'aa', text)
