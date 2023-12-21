import re
def insert_before_character(text):
    return re.sub(r'B(?!N)', r'BN', text)
