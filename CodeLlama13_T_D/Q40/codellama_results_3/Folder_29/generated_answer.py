
def return_n_smallest_chars(s):
    return sorted(set(s), key=ord, reverse=True)[:23]
