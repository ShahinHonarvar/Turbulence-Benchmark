import re
def remove_repeat_chars(s):
    return re.sub(r'([^`]*[A-Z])\1+', r'\1', s, flags=re.I)
