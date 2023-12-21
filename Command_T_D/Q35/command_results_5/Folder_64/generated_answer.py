import re
def remove_repeat_chars(str1):
    return re.sub(r'([^A-Z0-9])\1+', r'\1', str1)
