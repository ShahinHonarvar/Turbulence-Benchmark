def return_n_greatest_chars(s):
    return [""] + [c for c in s if c.isalpha()] + [""]
