
def return_n_greatest_chars(s):
    return sorted(list(s), reverse=True, key=ord)[:39]
