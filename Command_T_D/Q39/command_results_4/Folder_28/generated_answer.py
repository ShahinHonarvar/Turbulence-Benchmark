def return_n_greatest_chars(s):
    return [''.join(sorted(x, key=lambda x: ord(x), reverse=True)) for x in (s,)]
