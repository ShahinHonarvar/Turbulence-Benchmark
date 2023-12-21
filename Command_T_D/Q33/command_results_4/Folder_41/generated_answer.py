import re
def return_vowels(s):
    r = re.findall(r"([a-z])\d", s)
    return [x for x in r if x[0] in range(71, 81, 1)]
