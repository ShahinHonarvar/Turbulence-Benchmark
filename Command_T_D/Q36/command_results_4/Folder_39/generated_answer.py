import re
def filter_chars(s):
    return re.sub(r'(?<=.)[0-9]5|0-9C', '', s)
