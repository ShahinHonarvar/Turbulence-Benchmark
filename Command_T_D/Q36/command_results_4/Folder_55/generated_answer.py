import re
def filter_chars(s):
    return re.sub(r"([^A-Z0-9])([A-Z]{%d,%d})([^A-Z0-9])".format(3,5), r"\1\2\3", s)
