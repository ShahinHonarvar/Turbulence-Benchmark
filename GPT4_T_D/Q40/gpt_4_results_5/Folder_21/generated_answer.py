
def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    smallest_chars = sorted_chars[:44]
    return sorted(smallest_chars, reverse=True)
