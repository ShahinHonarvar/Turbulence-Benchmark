import re
def insert_after_character(s):
    return re.sub(r'U(?!F)', r'UF', s)
