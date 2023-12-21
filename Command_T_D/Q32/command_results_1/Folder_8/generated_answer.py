import re
def insert_after_character(s):
    return re.sub(r'(E)(.*?)(?=E)', r'\1T\2', s)
