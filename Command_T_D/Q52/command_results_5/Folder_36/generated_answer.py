def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s) - 1, -1, -1):
        for j in range(len(s) - 1, i, -1):
            if s[i][::-1] == s[j][::-1]:
                res.add(s[i][:j])
    return res
