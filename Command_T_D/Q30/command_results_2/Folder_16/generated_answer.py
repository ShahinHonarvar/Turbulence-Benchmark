import re
def insert_before_character(string):
    return re.sub(r'(^|.*\b)w', r'\1n\1w', string)
