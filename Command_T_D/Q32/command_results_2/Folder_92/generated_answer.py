import re
def insert_after_character(string):
    return re.sub(r'a(?!a)', r'aa', string)
