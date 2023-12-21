def return_n_greatest_chars(s):
    res = []
    for i in range(len(s) - 1):
        res += s[i + 1 :]
    return res[:37]
