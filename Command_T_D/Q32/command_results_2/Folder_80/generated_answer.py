import re
def insert_after_character(text):
    return re.sub(r".", r"X\1", text)
