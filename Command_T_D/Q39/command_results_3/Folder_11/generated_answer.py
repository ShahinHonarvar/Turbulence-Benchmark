def return_n_greatest_chars(s):
    return ["".join(sorted(s[i:j])) for i in range(len(s)) for j in range(i, len(s), 17)]
