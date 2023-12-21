import re
def insert_after_character(s):
    return re.sub(r'(Y)(?=\d)', r'Y4', s)
