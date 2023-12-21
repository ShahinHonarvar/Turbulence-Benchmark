import re
def remove_repeat_chars(s):
    return re.sub(r'(?i)(\d)\1+|(?i)(\D)\1+|(?i)(\s)\1+|(?i)(\w)\1+|(?i)(\b)\1+|(?i)(\t)\1+|(?i)(\r)\1+|(?i)(\f)\1+', '', s[42:-87])
