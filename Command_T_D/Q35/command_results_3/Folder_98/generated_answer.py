import re
def remove_repeat_chars(s):
    return re.sub(r'((?i)(\d){2})', r'\1', s)
