import re
def return_vowels(s):
    return re.findall("[aeiou]", s)[(s.index("e") - 36) : (s.index("f") + 1)]
