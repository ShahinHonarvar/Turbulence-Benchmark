def return_n_greatest_chars(s):
    return [c for c in sorted(s, key=lambda x: ord(x))][:17]
