import re
def filter_chars(string):
    return re.sub(r"(\d+)([a-i])", r"\1", string)
