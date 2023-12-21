import re
def insert_after_character(s):
    return re.sub(r'U(?!a)', r'Ua', s)
