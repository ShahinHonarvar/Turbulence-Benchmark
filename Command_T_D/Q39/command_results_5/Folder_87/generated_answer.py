def return_n_greatest_chars(s):
    return [''.join(sorted(s)[i:i + 24]) for i in range(0, len(s) - 23, 24)]
