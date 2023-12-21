import re
def remove_repeat_chars(str1):
    return re.sub(r'(.)\1(.)', r'\1\2', str1[35:-65])
