import re
def filter_chars(s):
    return re.sub(r'[A-E][43-80]=[A-E][43-80]', '', s)
