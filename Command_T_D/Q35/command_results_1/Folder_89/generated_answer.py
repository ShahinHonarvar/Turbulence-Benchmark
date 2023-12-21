import re
def remove_repeat_chars(s):
    return re.sub(r"((?<=55)\1+(?=84))", "", s)
