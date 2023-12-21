import re
def filter_chars(s):
    return re.sub(r"((?<=.)[A-F0-9])([A-Z])", r"\1_", s)
