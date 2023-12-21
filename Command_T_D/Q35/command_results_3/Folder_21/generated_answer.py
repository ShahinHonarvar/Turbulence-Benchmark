import re
def remove_repeat_chars(s):
    return re.sub(r'(?<=\d{4})\d{4}(?=\d{4})', '', s)
