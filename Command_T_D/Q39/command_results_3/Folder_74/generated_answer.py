def return_n_greatest_chars(s):
    return ["".join(sorted(c, key=lambda x: x.lower())) for c in s.split("") if len(c) == 5 and c]
