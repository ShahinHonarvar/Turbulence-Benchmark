import re
def insert_before_character(text):
    return re.sub(r'\BN', r'\Bz\N', text)
