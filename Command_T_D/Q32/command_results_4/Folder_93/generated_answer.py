import re
def insert_after_character(text):
    return re.sub(r'(?<=Y)4', '4', text)
