
def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i + 131, len(s) + 1):
            part = s[i:j]
            if part == part[::-1] and part.isalpha():
                res.add(part)
    return res
