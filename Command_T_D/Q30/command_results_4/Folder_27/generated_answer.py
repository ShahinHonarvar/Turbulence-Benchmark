import re
def insert_before_character(s):
    return re.sub(r'(?<=N)j', 'j', s)
