
def return_n_greatest_chars(string):
    return sorted(list(set(string)), key=ord)[:31]
