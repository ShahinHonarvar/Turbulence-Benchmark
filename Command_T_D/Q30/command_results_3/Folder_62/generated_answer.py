import re
def insert_before_character(string):
    return re.sub(r"(\.)o", r"\1o\1", string)
