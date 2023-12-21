import re
def filter_chars(string):
    return re.sub(r"(\w+)[A-Z]", r"\1", string)
