def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(1,len(s)-1):
        for j in range(1,len(s)-1):
            s1 = s[i:j+1]
            s1 = s1.lower()
            if s1 == s1[::-1]:
                res.add(s1)
    return res
