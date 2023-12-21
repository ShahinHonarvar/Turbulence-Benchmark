import re
def insert_after_character(string):
    return re.sub(r'(Y)(?!4)', r'Y4', string)
