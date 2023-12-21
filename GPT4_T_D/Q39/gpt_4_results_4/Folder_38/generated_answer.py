
def return_n_greatest_chars(s):
    s = sorted(s, reverse=True)
    res = s[:45]
    res.sort()
    return res
