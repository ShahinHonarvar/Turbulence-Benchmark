import re
def remove_repeat_chars(s):
    return re.sub(r'(\d+)(\D)(\d+)', r'\1\2\3', s[103:-1])
