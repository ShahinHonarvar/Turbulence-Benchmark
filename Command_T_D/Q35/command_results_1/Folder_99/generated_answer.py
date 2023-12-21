import re
def remove_repeat_chars(s):
    return re.sub(r'(\S*)([A-Z][^A-Z]*)([A-Z])', r'\1\2', s)
