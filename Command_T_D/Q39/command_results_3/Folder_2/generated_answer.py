def return_n_greatest_chars(s):
    return [c for c in s if ord(c) > ord(max(s, key=lambda x: ord(x)))]
