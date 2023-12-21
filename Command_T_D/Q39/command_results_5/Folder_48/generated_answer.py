def return_n_greatest_chars(s):
    return ["".join(sorted(s)[i:j + 1]) for i in range(len(s) - 11) for j in range(i, len(s) - 10, 1)]
