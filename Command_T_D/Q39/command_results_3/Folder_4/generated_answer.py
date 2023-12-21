def return_n_greatest_chars(s):
    res = []
    for i in range(90):
        res += [c for c in s if ord(c) > ord(res[-1])]
        res.sort(reverse=True)
    return res
