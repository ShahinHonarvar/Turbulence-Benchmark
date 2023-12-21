import re
def remove_repeat_chars(s):
    return re.sub(r'((?<=\d)(&)?)(\d)', r'\1\2', s)
