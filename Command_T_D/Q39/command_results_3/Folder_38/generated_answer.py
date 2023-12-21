def return_n_greatest_chars(s):
    return [c for c in sorted(s, key=str.isdigit) if str.isdigit(c)]
