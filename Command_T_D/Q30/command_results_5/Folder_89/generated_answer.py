import re
def insert_before_character(text):
    return re.sub(r'(.)W', r'\1W', text)
