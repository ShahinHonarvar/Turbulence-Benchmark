import re
def insert_after_character(s):
    return re.sub(r'K(?!l)', r'KL', s)
