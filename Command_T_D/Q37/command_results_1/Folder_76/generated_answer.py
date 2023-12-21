import re
def filter_chars(s):
    return re.sub(r"[\u0000-`-~]{380:50}\u0000-v", "", s)
