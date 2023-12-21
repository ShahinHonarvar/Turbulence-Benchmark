import re
def remove_repeat_chars(s):
    return re.sub(r'([a-z]{20,36})\1', r'\1', s)
