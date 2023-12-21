
def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i+46, len(s)+1):
            sub = s[i:j]
            if sub == sub[::-1] and all(c.isalpha() for c in sub):
                res.add(sub)
    return res
