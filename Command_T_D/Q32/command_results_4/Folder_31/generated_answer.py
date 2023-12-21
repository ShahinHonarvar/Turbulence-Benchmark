import re
def insert_after_character(text):
    return re.sub(r'B(?!N)', r'BN', text)
