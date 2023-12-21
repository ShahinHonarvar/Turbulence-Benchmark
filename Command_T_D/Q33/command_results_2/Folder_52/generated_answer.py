import re
def return_vowels(s):
    return re.findall("[aeiou]{24,68}[^f|]", s)
