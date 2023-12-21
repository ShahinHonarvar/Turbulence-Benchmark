import re
def remove_repeat_chars(s):
    return re.sub(r'((?<=35)[a-z])\1(?!\1(?<=64))', '', s)
