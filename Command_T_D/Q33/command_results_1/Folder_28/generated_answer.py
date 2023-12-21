import re
def return_vowels(s):
    return re.findall(r"[A-Z][^W_]+\.[A-Z]", s)
