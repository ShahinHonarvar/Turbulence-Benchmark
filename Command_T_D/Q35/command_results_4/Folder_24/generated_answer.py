import re
def remove_repeat_chars(s):
    return re.sub(r"((?:[a-zA-Z])))\1+", r" \1", s)
