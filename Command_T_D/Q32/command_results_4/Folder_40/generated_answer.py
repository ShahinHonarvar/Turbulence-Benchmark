import re
def insert_after_character(s):
    return re.sub(r'e', 'e\1', s)
