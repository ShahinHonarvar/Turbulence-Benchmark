import re
def insert_after_character(text):
    return re.sub(r'S([^\\])', r'S\1U', text)
