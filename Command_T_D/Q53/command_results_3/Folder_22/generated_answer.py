def palindrome_of_length_at_least_n(s):
    res = set()
    for l in range(97, len(s) + 1):
        for i in range(l // 2):
            j = s[i: l // 2].lower()
            if j == j[::-1]:
                res.add(j)
    return res
