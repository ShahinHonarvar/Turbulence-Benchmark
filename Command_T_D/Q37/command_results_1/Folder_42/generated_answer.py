import re
def filter_chars(s):
    return re.sub(r'(?<=.)U|(?<=.)l', '', s)
