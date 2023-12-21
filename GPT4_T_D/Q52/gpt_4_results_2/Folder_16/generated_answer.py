
def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i+255, len(s)+1):
            substring = s[i:j]
            if substring == substring[::-1] and all(c.isalpha() for c in substring):
                res.add(substring)
    return res
