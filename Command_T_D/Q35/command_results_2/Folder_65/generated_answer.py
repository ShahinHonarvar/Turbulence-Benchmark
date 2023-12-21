import re
def remove_repeat_chars(s):
    return re.sub(r"((?i)(?<=51)\1(?=76))", "", s)
