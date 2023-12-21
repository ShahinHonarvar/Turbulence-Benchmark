import re
def insert_after_character(string):
    return re.sub(r'(m)', r'\1N', string)
