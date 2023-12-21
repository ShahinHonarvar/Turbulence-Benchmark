def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s) + 1):
            tmp = s[i:j]
            if tmp == tmp[::-1]:
                res.add(tmp)
    return res
