import re
def filter_chars(s):
    return re.sub(r"[^0-9Q-Z]{%d,%d}(?=[^0-9Q-Z]{%d,%d})".format(299, 418, 299, 418), "", s)
