import re
def filter_chars(s):
    return re.sub(r'(?<=.)([a-z]{55,80})', '', s)
