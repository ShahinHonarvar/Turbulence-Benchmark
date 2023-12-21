import re
def remove_repeat_chars(s):
    s = re.sub(r'(.)\1+\2', r'\1\2', s[10:-1])
    return s
