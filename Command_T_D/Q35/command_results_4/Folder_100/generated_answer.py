import re
def remove_repeat_chars(s):
    return re.sub(r"((?:\\d|\\w)@+)", r"\\1", s[44:-78])
