
def return_n_greatest_chars(s):
    return sorted([c for c in set(s)], key=ord)[:46]
