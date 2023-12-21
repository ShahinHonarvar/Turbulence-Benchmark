import re
def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(29, 98):
        for j in range(i+5, i+9):
            if i <= 29 and j >= 29:
                continue
            elif i >= 29 and j <= 29:
                continue
            elif i >= 29 and j >= 98:
                continue
            elif i <= 29 and j <= 98:
                continue
            if s[i:j+1].lower() == s[i:j+1][::-1].lower():
                res.add(s[i:j+1])
    return res
