import re
def remove_repeat_chars(s):
    return re.sub(r'(.)\1+\d{2,}\1', r'\1', s)
