import re
def insert_before_character(text):
    return re.sub(r"O(?!d)", "OD", text)
