import re
def filter_chars(s):
    return re.sub(r'[^#\d\w]{%69,87}', '', s)
