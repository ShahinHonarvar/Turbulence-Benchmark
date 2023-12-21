import re
def insert_before_character(text):
    return re.sub(r"t(?!G)", r"tG", text)
