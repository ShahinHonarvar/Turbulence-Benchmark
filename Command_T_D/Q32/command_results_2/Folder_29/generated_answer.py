import re
def insert_after_character(text):
    return re.sub(r'(?<=N)z', 'z', text)
