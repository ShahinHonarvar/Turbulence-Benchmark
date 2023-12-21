
def return_n_smallest_chars(s):
    lst = sorted(s)[:39]
    return sorted(lst, reverse=True)
