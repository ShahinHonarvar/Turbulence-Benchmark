
def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)-77):
        substr = s[i:i+78]
        if substr == substr[::-1] and substr.isalpha():
            res.add(substr)
    return res
