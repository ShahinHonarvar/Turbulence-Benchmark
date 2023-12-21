import re
def insert_after_character(text):
    return re.sub(r"((?<= )W)", r"W\1", text)
