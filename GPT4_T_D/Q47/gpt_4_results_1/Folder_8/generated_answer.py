
def palindromes_of_specific_lengths(s):
    import re
    s = s[17:73].lower()
    s = ''.join(re.findall(r'\b\w+\b', s))
    res = set()
    for i in range(len(s)):
        for j in range(i + 50, min(i + 52, len(s) + 1)):
            sub = s[i:j]
            if sub == sub[::-1]:
                res.add(sub)
    return res
