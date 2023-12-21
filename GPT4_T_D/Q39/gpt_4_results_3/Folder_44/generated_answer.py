
def return_n_greatest_chars(s):
    s = sorted(s, reverse=True)
    s = s[:73]
    s.sort()
    return s
