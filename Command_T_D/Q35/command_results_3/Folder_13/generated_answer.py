import re
def remove_repeat_chars(s):
    return re.sub(r'(.)\1(.)\2(.)\3', r'\1\2\3', s)
