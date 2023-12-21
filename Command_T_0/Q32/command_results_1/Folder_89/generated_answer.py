import re
def insert_after_character(s):
    return re.sub(r'(.)W', r'\1W', s)
