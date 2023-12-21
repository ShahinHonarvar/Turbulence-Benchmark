def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(len(s)):
        for j in range(i, len(s)-1):
            if s[i:j+1].lower() == s[j:i+1].lower():
                res.add(s[i:j+1])
    return res
