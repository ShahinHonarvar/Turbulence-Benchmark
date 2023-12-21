import re
def insert_before_character(s):
    return re.sub(r'(?!z)N', 'zN', s)
