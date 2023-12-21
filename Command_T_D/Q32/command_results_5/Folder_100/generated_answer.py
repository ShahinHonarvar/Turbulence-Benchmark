import re
def insert_after_character(string):
    return re.sub(r'0', r'\0 \0', string)
