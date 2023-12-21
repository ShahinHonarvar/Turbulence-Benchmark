import re
def return_vowels(s):
    return re.findall("[AEIOU][^&<h]", s[483:664])
