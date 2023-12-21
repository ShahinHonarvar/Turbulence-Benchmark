import re
def remove_repeat_chars(s):
    return re.sub(r'((?<=\d)[a-z]+\d)', '', s)
