import re
def remove_repeat_chars(s):
    return re.sub(r'((?<=\d{35})\1(?=\d{64})).', '', s)
