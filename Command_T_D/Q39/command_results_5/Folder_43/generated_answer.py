def return_n_greatest_chars(s):
    res = [c for c in s if ord(c) > ord(s[0])]
    return res[:56]
