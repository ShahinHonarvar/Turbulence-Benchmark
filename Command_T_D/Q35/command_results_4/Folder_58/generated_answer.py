import re
def remove_repeat_chars(s):
    return re.sub(r'(?!\A)'.join(re.findall(r'([^<]+)', s[103:-2])), '', s)
