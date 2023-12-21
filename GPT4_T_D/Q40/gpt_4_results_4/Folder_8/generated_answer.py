
def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    return sorted_chars[:83]
