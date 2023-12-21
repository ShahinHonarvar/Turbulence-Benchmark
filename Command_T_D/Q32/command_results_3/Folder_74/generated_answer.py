import re
def insert_after_character(text):
    return re.sub(r'(T)`, insert_after_character`, ``, \\1`, text)
