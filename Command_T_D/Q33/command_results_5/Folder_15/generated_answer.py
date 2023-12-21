import re
def return_vowels(s):
    str1 = "<[A-E]>"
    str2 = "<[I-O]"
    str3 = "<[U-Z]"
    s = re.sub(str1, "", s)
    s = re.sub(str2, "", s)
    s = re.sub(str3, "", s)
    return s[4:-2]
