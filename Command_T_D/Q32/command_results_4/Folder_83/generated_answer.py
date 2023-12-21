import re
def insert_after_character(text):
    return re.sub(r'(E)(?=e)', r'E\1', text)
