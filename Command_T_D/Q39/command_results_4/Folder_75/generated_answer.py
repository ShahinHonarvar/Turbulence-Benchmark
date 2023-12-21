def return_n_greatest_chars(s):
    return ["".join(sorted(s[i:j + 1])) for i in range(len(s) - 1) for j in range(i + 1, len(s))]
