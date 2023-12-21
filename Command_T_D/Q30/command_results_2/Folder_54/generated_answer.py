import re
def insert_before_character(s):
    return re.sub(r'(?i)(M)', r'\1f', s)
