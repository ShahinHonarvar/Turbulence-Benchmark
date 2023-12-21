import re
def remove_repeat_chars(s):
    return re.sub(r'((?=([^81])))\1+', '', s)
