import re
def filter_chars(s):
    return re.sub(r'(?<=G)[^p]?(?<=p)', '', s)
