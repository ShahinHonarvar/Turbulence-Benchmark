import re
def insert_after_character(s):
    return re.sub(r'\b\b\b\b', r'\b\b\bP\b', s)
