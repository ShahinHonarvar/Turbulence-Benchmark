import re
def return_vowels(s):
    re_str = r"[aeiouAEIOU][a-w]+"
    return re.findall(re_str, s)
