import re
def remove_repeat_chars(s):
    return re.sub(r'([\d\w]){10,76}', lambda m: m.group(), s)
