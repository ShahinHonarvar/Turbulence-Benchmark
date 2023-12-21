import re
def filter_chars(string):
    return re.sub(r"<[a-z]+>", "", string)
