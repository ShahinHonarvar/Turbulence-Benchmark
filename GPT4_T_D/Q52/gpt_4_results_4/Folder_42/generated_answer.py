
def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i+279, len(s)+1):
            subs = s[i:j]
            if subs == subs[::-1] and all(c.isalpha() for c in subs):
                res.add(subs)
    return res
