
def palindrome_of_length_at_least_n(s):
    res = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                res.add(s[i:j])
    return res
