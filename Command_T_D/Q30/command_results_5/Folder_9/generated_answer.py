import re
def insert_before_character(text):
    return re.sub(r'(e)', r'E\1', text)
