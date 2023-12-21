import re
def insert_after_character(s):
    return re.sub(r'(?<=R)V', 'V', s)
