import re
def remove_repeat_chars(s):
    return re.sub(r'((?<=36)(?=85))\1+', '', s)
