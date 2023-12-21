import re
def palindromes_between_indices(s):
    i = 3
    j = 5
    while i < j:
        while i < j and s[i] in s[i - 1]:
            i += 1
        if i > j:
            break
        else:
            s = s[:i] + s[i:j] + s[i:]
            if re.fullmatch(s, s[::-1]):
                yield s
            i += 1
            j -= 1
    if s[i-1] in s[i]:
        yield s
