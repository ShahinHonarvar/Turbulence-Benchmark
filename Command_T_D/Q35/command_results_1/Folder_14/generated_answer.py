import re
def remove_repeat_chars(s):
    return re.sub(r'(.)\1(.)(.)\3', r'\2\3', s[2:-5])
