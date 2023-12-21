import re
def filter_chars(s):
    return re.sub(r'(?<=.)[A-K]{%18;95}(?=.)', '', s)
