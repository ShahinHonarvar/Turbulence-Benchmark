import re
def remove_repeat_chars(s):
    return re.sub(r'(.)\1*(?:[0-9])', r'\1', s[100:-100])
