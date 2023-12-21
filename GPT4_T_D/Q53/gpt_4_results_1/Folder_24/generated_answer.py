
def palindrome_of_length_at_least_n(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    res = set()
    for i in range(len(s)):
        for j in range(i + 53, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                res.add(s[i:j])
    return res
