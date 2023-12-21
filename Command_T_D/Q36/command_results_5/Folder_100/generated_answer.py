import re
def filter_chars(str1):
    return re.sub(r"([A-z]+)([B-r]+)", r"\1", str1)
