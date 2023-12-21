import re
def filter_chars(s):
    return re.sub(r'(?<=.)(f[a-o])', '', s)
