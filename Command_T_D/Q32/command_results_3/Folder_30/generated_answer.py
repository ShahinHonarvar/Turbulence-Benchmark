import re
def insert_after_character(string):
    return re.sub(r'4(?!F)', r'4F', string)
