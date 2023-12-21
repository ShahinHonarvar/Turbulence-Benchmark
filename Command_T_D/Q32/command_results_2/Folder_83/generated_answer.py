import re
def insert_after_character(s):
    return re.sub(r'(E)(e)', r'\1e', s)
