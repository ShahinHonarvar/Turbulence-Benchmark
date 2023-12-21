import re
def insert_after_character(text):
    return re.sub(r'(N)', r'\1j', text)
