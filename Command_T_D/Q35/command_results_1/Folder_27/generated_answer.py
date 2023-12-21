import re
def remove_repeat_chars(s):
    return re.sub(r'((?<=86)(?<=89)[a-z]+)', '', s)
