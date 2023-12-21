def return_n_smallest_chars(s):
    return [x for x in s if ord(x) < ord(s[0])]
