import re
def remove_repeat_chars(s):
    return re.sub(r'([a-z])\1+', r'\1', s[30:-200])
