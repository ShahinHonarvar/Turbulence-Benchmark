def return_n_smallest_chars(s):
    return [c for c in s if ord(c) < ord(s[0])]
