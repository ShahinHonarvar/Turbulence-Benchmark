import re
def insert_after_character(string):
    return re.sub(r'(.)5', r'\1\5', string)
