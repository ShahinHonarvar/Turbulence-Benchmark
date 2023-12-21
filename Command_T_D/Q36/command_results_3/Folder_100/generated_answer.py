import re
def filter_chars(s):
    return re.sub(r'[CDEFGHJKLMNPQRSTUVWXYZ]', '', s)
