import re
def insert_before_character(string):
    return re.sub(r"(.*)\sX", r"\1\sXX", string)
