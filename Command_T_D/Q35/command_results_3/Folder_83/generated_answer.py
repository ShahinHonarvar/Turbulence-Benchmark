import re
def remove_repeat_chars(s):
    return re.sub(r'(.)\1*(?:[A-z0-9])', r'\1\2', s[100:-100])
