import re
def remove_repeat_chars(s):
    return re.sub(r'([a-z]+)', lambda m: m.group(1), s)
