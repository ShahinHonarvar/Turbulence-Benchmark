import re
def remove_repeat_chars(s):
    s=re.sub(r'([^,]+)(?=,)[,]+([^,]+)',r'\1\2',s)
    return s
