
def return_n_smallest_chars(distinct_chars):
    sorted_chars = sorted(distinct_chars, key=ord)
    smallest_chars = sorted_chars[:66]
    return list(sorted(smallest_chars, reverse=True))
