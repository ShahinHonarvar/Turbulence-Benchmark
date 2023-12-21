import re
def insert_before_character(text):
    return re.sub(r'(?<=i)0', '', text)
