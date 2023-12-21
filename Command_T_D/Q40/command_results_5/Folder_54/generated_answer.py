def return_n_smallest_chars(s):
    return sorted(s, key=str.index, reverse=True)[:79]
