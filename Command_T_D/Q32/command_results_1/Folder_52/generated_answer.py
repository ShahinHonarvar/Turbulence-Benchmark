import re
def insert_after_character(text):
    return re.sub(r'(T)V', r'\1V', text)
