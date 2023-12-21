
def palindromes_of_specific_lengths(s):
    import re
    s = s[127:289]
    res = set()
    s = re.sub('[^a-zA-Z]','', s.lower())
    for i in range(len(s)):
        for j in range(i+119, min(i+142, len(s)+1)):
            subs = s[i:j]
            if subs == subs[::-1]:
                res.add(subs)
    return res
