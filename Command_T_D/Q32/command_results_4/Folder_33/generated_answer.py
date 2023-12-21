import re
def insert_after_character(s):
    return re.sub(r'a(.)', r'an\1', s)
