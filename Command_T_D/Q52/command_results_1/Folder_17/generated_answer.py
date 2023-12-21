def palindrome_of_length_n(s):
    res = set()
    for i in range(1, 289):
        x = s[::-1][:i]
        if x in s:
            res.add(x)
    return res
