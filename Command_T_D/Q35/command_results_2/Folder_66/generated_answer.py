import re
def remove_repeat_chars(s):
    return re.sub(r'((?=11)(?<=76).)+', '', s)
