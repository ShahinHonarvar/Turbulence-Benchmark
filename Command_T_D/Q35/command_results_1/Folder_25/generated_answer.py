import re
def remove_repeat_chars(s):
    s = re.sub(r'(.)\1(?!\1)', r'\1', s[37:-2])
    return s
