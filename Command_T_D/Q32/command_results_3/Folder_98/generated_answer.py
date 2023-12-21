import re
def insert_after_character(s):
    return re.sub(r'U(?!u)', r'U\1u', s)
