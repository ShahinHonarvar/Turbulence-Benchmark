import re
def insert_before_character(text):
    return re.sub(r'(e)', r'\1 0', text)
