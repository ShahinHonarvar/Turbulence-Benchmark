def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(len(s) + 1):
        j = 0
        while i - j >= 4:
            if s[i - 1] == s[j]:
                res.add(s[i - 1])
                j += 1
            else:
                break
    return res
