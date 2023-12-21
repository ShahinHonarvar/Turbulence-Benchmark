import re
def insert_before_character(string):
    return re.sub(r'(?<=E)T', r'T\1', string)
