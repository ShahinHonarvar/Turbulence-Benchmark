import re
def insert_before_character(s):
    return re.sub(r'(e)', r'e\1', s)
