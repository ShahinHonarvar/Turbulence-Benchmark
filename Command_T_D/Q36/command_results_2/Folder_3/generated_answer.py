import re
def filter_chars(s):
    return re.sub(r"![^?]{%d,%d}".format(42, 78), "", s)
