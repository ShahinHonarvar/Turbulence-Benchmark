import re
def remove_repeat_chars(s):
    return re.sub(r'(\w)(?=\1)', '', s, flags=re.I)
