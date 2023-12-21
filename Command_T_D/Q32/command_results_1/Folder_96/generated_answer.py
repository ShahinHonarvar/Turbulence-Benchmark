import re
def insert_after_character(s):
    return re.sub(r'a(?!A)', r'aa', s)
