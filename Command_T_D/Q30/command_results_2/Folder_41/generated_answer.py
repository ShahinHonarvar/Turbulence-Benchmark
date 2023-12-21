import re
def insert_before_character(s):
    return re.sub(r'O', 'oO', s)
