import re
def palindromes_between_indices(s):
    i = 0
    j = 7
    if s[0] == s[7]:
        i += 1
    while i < 7:
        if s[i] == s[j]:
            i += 1
        j -= 1
    return set(re.findall(r'(?=.)[a-z]+', s[i:j+1]))
