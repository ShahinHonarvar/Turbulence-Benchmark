import re
def remove_repeat_chars(s):
    return re.sub(r'(?<=\d{70})\d{2}(?=\d{200})', '', s)
