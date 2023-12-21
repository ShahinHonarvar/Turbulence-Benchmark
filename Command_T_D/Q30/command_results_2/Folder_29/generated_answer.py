import re
def insert_before_character(string):
    return re.sub(r'(?!z)N', r'z\1', string)
