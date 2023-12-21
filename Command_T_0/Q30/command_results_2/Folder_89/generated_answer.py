import re
def insert_before_character(s):
    return re.sub(r'(.)W', r'\1W', s)
