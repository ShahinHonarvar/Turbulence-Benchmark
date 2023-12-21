import re
def remove_repeat_chars(s):
    return re.sub(r'([^3^9]*)\1+', r'\1', s)
