import re
def insert_before_character(text):
    return re.sub(r'(S)', r'\1U', text)
