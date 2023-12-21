import re
def filter_chars(s):
    return re.sub(r'(?<=.)[H-e]', '', s)
