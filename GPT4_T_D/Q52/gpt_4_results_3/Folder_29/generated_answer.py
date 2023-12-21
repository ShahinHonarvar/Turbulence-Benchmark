
def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i + 19, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                res.add(substr)
    return res
