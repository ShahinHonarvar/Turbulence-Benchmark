import re
def remove_repeat_chars(str1):
    str1 = re.sub(r'(.)\1+', r'\1', str1[16:-87])
    return str1
