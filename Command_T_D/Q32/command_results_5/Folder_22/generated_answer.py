import re
def insert_after_character(s):
    return re.sub(r'U(?!U)U', 'UU', s)
