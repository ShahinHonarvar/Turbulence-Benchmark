import re
def insert_after_character(string):
    return re.sub(r'(?<=i)i', r'ii', string)
