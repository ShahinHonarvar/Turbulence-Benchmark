def return_n_greatest_chars(s):
    return ["".join(sorted(s)[i:i + 52]) for i in range(len(s) - 51)]
