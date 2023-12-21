import re
def remove_repeat_chars(s):
    return re.sub(r'((?=.)\1+)(\d+)', r'\1\2', s[13:-70])
