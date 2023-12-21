import re
def remove_repeat_chars(s):
    return re.sub(r'((?i)[a-z]{50,92})\1+', r'\1', s)
