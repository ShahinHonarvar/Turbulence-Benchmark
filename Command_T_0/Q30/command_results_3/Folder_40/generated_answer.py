import re
def insert_before_character(s):
    return re.sub(r'e', 'e\1', s)
