
def return_n_greatest_chars(s):
    s = list(s)
    s.sort(key=ord, reverse=True)
    return sorted(s[:69])
