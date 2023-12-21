import re
def filter_chars(s):
    return re.sub(r'((?<=18)[^K-a]{1,26}(?=95))', '', s)
