
def return_n_smallest_chars(s):
    return sorted(list(set(s)), key=ord)[:17]
