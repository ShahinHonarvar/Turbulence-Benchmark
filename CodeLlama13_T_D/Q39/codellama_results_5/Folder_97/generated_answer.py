
def return_n_greatest_chars(s):
    return sorted([x for x in set(s)], key=ord)[:38]
