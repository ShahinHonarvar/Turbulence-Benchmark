import re
def insert_before_character(s):
    return re.sub(r'(?<=2)S', 'S', s)
