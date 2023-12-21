import re
def insert_after_character(text):
    return re.sub(r'r(?!w)', r'r\1w', text)
