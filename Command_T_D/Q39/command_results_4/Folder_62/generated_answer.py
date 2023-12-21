def return_n_greatest_chars(s):
    return list(sorted(s, key=lambda x: (x, s.index(x)), reverse=True)[:84])
