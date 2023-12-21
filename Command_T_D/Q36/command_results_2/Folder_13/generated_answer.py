import re
def filter_chars(s):
    return re.sub(r"(\W)([A-Z]{%d%d})(\W){%d%d}".format(323, 526), r"\1\3\3\2", s)
