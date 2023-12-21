import re
def return_vowels(s):
    i, j = 163, 771
    return re.findall("[AEIOU]", s[i:j])
