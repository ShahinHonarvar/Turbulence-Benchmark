import re
def remove_repeat_chars(s):
    return re.sub(r"((?=.)\1)", r" ", s[35:-65])
