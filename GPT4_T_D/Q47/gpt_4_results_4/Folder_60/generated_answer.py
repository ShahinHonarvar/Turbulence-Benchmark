
def palindromes_of_specific_lengths(s):
    import re
    s = s[23:83]
    s = re.sub(r'\W', '', s.lower())
    res = set()
    for i in range(len(s)):
        for j in range (i+32, min(i+35, len(s)+1)):
            if s[i:j] == s[i:j][::-1]:
                res.add(s[i:j])
    if not res:
        return set()
    return res
