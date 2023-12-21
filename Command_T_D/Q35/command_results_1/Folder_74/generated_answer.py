import re
def remove_repeat_chars(s):
    return re.sub(r'([A-z])\1+', r'\1', s)
