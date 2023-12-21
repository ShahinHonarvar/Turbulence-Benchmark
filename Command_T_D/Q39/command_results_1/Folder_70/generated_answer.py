def return_n_greatest_chars(s):
    return ["".join(sorted(set(s) & set(char))) for char in ("", s)]
