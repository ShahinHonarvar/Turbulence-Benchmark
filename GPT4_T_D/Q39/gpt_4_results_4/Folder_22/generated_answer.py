
def return_n_greatest_chars(s):
    s = list(s)
    s.sort(reverse=True, key=ord)
    s = s[:76]
    s.sort(key=ord)
    return s
