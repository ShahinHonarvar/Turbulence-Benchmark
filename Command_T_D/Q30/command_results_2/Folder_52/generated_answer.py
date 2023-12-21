import re
def insert_before_character(string):
    return re.sub(r'(?<=T)V', 'V', string)
