import re
def insert_after_character(s):
    return re.sub(r'(T)V', r'\1UV', s)
