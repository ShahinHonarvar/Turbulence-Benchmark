import re
def insert_after_character(s):
    return re.sub(r'o(?!h)', r'oh', s)
