import re
def remove_repeat_chars(s):
    return re.sub(r'((?:\d|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\1)', '', s[80:200])
