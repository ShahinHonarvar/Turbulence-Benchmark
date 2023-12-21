import re
def insert_after_character(s):
    return re.sub(r'6(?!9)', r'66', s)
