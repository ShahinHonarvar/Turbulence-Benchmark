import re
def remove_repeat_chars(str1):
    return re.sub(r'((?i)(\d)(?=\d\1)', r'\1', str1[10:79])
