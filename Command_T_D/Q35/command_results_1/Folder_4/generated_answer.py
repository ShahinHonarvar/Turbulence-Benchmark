import re
def remove_repeat_chars(s):
    return re.sub(r'[a-z]{%d,%d}{%d,%d}'.format(49, 74, 49, 74), '', s)
