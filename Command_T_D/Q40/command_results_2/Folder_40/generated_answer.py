def return_n_smallest_chars(s):
    return [c for c in s if ord(c) in range(ord(min(s)), ord(max(s)) + 1)]
