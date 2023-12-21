import re
def filter_chars(s):
    return re.sub(r"([Ee][a-t]{,3})", "", s)
