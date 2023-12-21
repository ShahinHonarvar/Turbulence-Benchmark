import re
def remove_repeat_chars(str1):
    return re.sub(r'(.)\1(.)\2(.)\3(.)\4(.)\5', r'\1\2\3\4\5', str1)
