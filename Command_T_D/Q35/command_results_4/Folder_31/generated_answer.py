import re
def remove_repeat_chars(s):
    return re.sub(r'(?<=\d{33})\d{2}((?=\d{33})\d{2})', '', s)
