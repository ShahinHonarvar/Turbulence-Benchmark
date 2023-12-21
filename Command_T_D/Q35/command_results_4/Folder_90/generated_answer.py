import re
def remove_repeat_chars(s):
    return re.sub(r'((?i)(\d\d\d)(?=\d\d))', r'\1', s)
