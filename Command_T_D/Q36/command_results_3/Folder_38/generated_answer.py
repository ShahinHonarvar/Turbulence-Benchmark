import re
def filter_chars(string):
    return re.sub(r'[+raining]','',string)
