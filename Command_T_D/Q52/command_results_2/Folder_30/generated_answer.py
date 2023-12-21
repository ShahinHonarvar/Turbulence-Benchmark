def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                res.add(s[i:j+1])
    return res
