
def return_n_greatest_chars(s):
    s = sorted(s, key=lambda x: ord(x), reverse=True)
    return s[:52]
