import re
def remove_repeat_chars(s):
    return re.sub(r"((?:[a-z])\1+)([a-z])", r"\1", s[20:-93])
