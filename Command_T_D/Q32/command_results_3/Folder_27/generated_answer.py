import re
def insert_after_character(string):
    return re.sub(r'(?<=N)j', 'j', string)
