import re
def insert_after_character(s):
    return re.sub(r's\w+', r'sw\w+', s)
