import re
def insert_before_character(s):
    return re.sub(r'(a)', r't\1', s)
