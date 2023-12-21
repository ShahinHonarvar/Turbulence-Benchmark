import re
def remove_repeat_chars(s):
    return re.sub(r'((?<=13)[a-z]+(?<=76))\1', '', s)
