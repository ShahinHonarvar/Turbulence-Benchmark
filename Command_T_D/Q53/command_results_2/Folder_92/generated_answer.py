def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(11):
        for j in range(len(s) - i):
            if s[j:j + i] == s[j:j + i][::-1]:
                res.add(s[j:j + i])
    return res
