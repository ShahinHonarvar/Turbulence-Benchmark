import re
def remove_repeat_chars(str1):
    str1 = str(str1)[57:-85]
    return re.sub(r'([a-z])\1+', r'\1', str1)
