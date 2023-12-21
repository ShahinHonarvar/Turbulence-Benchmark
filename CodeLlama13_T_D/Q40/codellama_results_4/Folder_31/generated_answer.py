
def return_n_smallest_chars(s):
    return sorted([x for x in s], key=ord, reverse=True)[:70]
