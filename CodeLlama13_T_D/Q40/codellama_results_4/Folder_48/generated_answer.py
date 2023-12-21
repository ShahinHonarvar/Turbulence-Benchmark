
def return_n_smallest_chars(string):
    lst = sorted([c for c in set(string)])
    return lst[:12]
