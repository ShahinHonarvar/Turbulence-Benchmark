import re
def insert_after_character(text):
    return re.sub(r'(e)([a-z])', r'\1E\2', text)
