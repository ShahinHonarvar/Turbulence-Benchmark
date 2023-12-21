
def return_n_greatest_chars(s):
    s = list(set(s))
    s.sort(key=ord, reverse=True)
    return s[:24]
