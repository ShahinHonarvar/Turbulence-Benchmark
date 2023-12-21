import re
def insert_before_character(s):
    return re.sub(r'(?<=w)', 'n', s)
