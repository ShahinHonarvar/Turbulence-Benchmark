import re
def remove_repeat_chars(str1):
    return re.sub(r'(.)\1+\d+', r'\1', str1[56:-90])
