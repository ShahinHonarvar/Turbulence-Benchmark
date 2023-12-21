import re
def insert_after_character(string):
    return re.sub(r'K(?!l)', r'KL', string)
