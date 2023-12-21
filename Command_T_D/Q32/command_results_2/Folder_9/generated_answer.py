import re
def insert_after_character(s):
    return re.sub(r'e\b', 'E\b', s)
