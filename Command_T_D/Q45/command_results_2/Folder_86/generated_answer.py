import re
def palindromes_between_indices(s):
    str_len = len(s)
    pal = set()
    for i in range(str_len):
        for j in range(i + 6, min(str_len - 1, i + 9)):
            if i >= j:
                continue
            if s[i:j] == s[j:i][::-1]:
                pal.add(s[i:j])
    return pal
