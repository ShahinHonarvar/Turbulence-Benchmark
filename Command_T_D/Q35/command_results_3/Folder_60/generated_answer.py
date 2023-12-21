import re
def remove_repeat_chars(str1):
    return re.sub(r'([a-z])\1+', r'\1', str1[38:-2])
