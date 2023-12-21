import re
def insert_before_character(string):
    return re.sub(r'(e)', r'0\1', string)
