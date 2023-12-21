import re
def insert_after_character(text):
    return re.sub(r'A(?!a)', r'A\1a', text)
