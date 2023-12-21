def return_n_greatest_chars(s):
    res = []
    for i in range(len(s)):
        res += [i] * (ord(s[i]) > ord(res[-1]) or len(res) == 37)
    return res
