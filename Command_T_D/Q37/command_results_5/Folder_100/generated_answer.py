import re
def filter_chars(s):
    return re.sub(r'(^|.*[A-Z])([J-Q].).*([A-Z]|$)', r'\1\3', s)
