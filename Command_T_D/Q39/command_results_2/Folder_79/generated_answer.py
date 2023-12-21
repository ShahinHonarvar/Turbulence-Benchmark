def return_n_greatest_chars(s):
    return [c for c in sorted(set(s), key=lambda c: ord(c)) if ord(c) <= 82][:82]
