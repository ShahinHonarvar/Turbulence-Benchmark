def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j] == s[j:i]:
                res.add(s[i:j])
    return res
