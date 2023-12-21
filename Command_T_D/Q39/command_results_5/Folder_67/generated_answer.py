def return_n_greatest_chars(s):
    return sorted(s, key=lambda c: ord(c), reverse=True)[:66]
