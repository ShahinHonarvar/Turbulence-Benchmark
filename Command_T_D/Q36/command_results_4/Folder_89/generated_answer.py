import re
def filter_chars(s):
    return re.sub(r'([\u0057-\u0069])', '', s)
