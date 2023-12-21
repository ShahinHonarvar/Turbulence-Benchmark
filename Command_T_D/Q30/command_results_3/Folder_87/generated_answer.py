import re
def insert_before_character(text):
    return re.sub(r'(?<=m)N', r'N\1', text)
