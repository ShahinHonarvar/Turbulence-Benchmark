import re
def insert_before_character(s):
    return re.sub(r"( )", r"\1\ ", s)
