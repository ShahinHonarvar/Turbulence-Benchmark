def return_n_greatest_chars(s):
    return ["".join(sorted(s)[i:i + 3]) for i in range(len(s) - 2)]
