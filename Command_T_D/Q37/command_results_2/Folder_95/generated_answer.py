import re
def filter_chars(s):
    return re.sub(r"((?<=.)\d{5})([a-z])((?=\.)\d{5})", r"\2", s)
