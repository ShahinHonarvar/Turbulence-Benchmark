
def return_n_greatest_chars(s):
    return sorted(sorted(s, key=ord)[-2:])
