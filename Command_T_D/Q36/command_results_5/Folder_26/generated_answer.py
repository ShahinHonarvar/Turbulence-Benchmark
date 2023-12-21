import re
def filter_chars(string):
    return re.sub(r"([A-Z][a-z]*)", r" ", string)
