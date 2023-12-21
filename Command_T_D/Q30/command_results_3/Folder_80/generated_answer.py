import re
def insert_before_character(s):
    return re.sub(r'(.)X(.)', r'\1XX\2', s)
