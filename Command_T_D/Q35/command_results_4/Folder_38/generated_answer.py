import re
def remove_repeat_chars(str1):
    return re.sub(r'((?<=\s[0-9])\1+)(?=\s[0-9])', '', str1[36:-85])
