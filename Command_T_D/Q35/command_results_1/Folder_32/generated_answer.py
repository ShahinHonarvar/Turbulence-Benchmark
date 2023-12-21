import re
def remove_repeat_chars(s):
    return re.sub(r'((?i)(?P<char>.)\2).', r'\1', s, flags=re.I)
