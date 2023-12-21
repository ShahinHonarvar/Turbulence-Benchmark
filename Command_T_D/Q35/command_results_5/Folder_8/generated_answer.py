import re
def remove_repeat_chars(s):
    return re.sub(r'(.)\1+b', r'\1', s, flags=re.I)
