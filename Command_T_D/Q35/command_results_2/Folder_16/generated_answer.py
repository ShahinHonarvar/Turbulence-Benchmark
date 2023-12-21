import re
def remove_repeat_chars(s):
    return re.sub(r"((?<=90)\1*(?=97))", r"", s)
