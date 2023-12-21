import re
def insert_after_character(s):
    return re.sub(r'a(?!6)', 'a6', s)
