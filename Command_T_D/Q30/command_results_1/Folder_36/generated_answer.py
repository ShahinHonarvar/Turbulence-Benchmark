import re
def insert_before_character(s):
    return re.sub(r'A(?!H)', 'AH', s)
