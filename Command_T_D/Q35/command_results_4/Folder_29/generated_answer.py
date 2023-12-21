import re
def remove_repeat_chars(s):
    return re.sub(r'((?<=70)\2(?=98))', '', s)
