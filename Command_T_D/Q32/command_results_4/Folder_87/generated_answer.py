import re
def insert_after_character(text):
    return re.sub(r"m", r"mN", text)
