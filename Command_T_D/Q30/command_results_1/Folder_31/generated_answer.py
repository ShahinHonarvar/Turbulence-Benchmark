import re
def insert_before_character(s):
    return re.sub(r'(?<=B)N', 'N', s)
