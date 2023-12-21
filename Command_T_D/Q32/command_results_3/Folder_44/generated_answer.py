import re
def insert_after_character(text):
    return re.sub(r'(g)([a-z])', r'gM\1', text)
