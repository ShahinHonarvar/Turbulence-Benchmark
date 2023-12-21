import re
def insert_after_character(s):
    return re.sub(r'(E)(?=f)', r'Ef', s)
