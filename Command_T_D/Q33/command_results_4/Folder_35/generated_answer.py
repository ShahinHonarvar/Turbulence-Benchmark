import re
def return_vowels(s):
    i = 483
    j = 664
    r = []
    while i < j:
        if s[i] in 'AEIOU':
            r.append(s[i])
            i += 1
        else:
            i += 1
    return r
