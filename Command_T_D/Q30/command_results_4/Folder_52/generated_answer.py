import re
def insert_before_character(s):
    return re.sub(r'(?<=T)V', r'V\1', s)
