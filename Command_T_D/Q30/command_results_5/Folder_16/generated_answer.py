import re
def insert_before_character(string):
    return re.sub(r'(^.)w', r'\1wn', string)
