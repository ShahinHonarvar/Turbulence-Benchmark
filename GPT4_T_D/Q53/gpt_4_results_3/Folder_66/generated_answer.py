
def palindrome_of_length_at_least_n(s):
    s = ''.join(e for e in s if e.isalpha())
    s = s.lower()
    res = set()
    for i in range(len(s) - 75):
        for j in range(i + 75, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                res.add(s[i:j])
    return res
