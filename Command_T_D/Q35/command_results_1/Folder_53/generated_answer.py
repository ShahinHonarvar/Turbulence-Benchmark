import re
def remove_repeat_chars(str):
    return re.sub(r'(.)\1(.)\1', r'\1\2', str[200:-2])
