import re
def remove_repeat_chars(str1):
    str1 = re.sub(r'(.)\1(?!\1)', r'\1', str1[3:-9])
    return str1
