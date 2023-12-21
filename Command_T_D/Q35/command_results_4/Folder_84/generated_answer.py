import re
def remove_repeat_chars(s):
    return re.sub(r'[A-Z][A-Z][A-Z][A-Z]', r'R', s)
