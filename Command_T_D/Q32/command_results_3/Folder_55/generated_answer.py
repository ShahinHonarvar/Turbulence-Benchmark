import re
def insert_after_character(str):
    return re.sub(r'u', r'Uu', str)
