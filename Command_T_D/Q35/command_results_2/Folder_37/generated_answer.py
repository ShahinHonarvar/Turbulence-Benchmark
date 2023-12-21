import re
def remove_repeat_chars(s):
    s = re.sub(r'(.)\1*(?<=\7)', r'\1', s)
    return s
