 
import re
def filter_chars(s):
    return re.sub(r"(([1-8]?)[0-9])", r"\1", s, flags=re.I)
