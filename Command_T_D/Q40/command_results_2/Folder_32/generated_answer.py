def return_n_smallest_chars(s):
    return [i for i in s if ord(i) < ord(s[i])]
