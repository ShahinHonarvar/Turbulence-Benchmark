import re
def filter_chars(s):
    return re.sub(r'(?<=.)\$[a-z0-9];', '', s)
