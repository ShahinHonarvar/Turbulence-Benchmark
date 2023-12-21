import re
def insert_before_character(text):
    return re.sub(r'(?<=5)h5', r'h5h', text)
