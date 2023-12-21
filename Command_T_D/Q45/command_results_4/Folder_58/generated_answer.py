import re
def palindromes_between_indices(s):
    i = 0
    j = 6
    while i < j:
        i += 1
        j = s[i - 1] + s[j - 1] + s[i:j]
        if re.match(r'(.*[a-z])[a-z]*\1', j, flags=re.I):
            yield j
        else:
            j = s[i - 1] + s[j - 1] + s[i:j]
            if re.match(r'(.*[a-z])[a-z]*\1', j, flags=re.I):
                yield j
