import re
def remove_repeat_chars(s):
    s = re.sub(r'(.)\1+', r'\1', s[77:-84])
    return s
