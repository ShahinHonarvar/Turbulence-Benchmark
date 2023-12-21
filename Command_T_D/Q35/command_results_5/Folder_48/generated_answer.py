import re
def remove_repeat_chars(s):
    return re.sub(r'(\d+)(?=\d\1)', r'\1', s[409:-1])
