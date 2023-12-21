import re
def filter_chars(s):
    return re.sub(r'\A(.*?)\((l inclusive).*?(\d+)\)', r'\1(\2)\3', s)
