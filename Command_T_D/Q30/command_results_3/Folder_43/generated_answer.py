import re
def insert_before_character(s):
    return re.sub(r't', 'G\1', s)
