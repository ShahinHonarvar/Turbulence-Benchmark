
def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i + 37, len(s) + 1):
            subset = s[i:j]
            if subset == subset[::-1] and subset.isalpha():
                res.add(subset)
    return res
