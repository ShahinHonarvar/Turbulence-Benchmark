import re
def remove_repeat_chars(s):
    return re.sub(r'((?<=\d)[a-z])\1+', '', s[36:-52])
