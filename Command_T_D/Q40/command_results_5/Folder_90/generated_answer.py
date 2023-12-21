def return_n_smallest_chars(s):
    return [c for c in sorted(s, key=lambda x: ord(x))][:24]
