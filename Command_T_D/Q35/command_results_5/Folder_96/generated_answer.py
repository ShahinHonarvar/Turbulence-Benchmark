import re
def remove_repeat_chars(s):
    s = re.sub(r"((?<=\d)[a-z])\1+", "", s[60:-200])
    return s
