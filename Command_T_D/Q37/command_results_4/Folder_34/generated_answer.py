import re
def filter_chars(s):
    return re.sub(r'(?!\d)\([0-9]{1,6}\)', '', s)
