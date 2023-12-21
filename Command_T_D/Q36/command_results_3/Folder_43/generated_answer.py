import re
def filter_chars(string):
    return re.sub(r'[A-z][^A-i]', '', string)
