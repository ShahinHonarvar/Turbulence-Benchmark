import re
def insert_before_character(string):
    return re.sub(r'(?<=.)R', r'\1V', string)
