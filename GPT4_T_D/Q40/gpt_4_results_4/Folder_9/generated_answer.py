
def return_n_smallest_chars(s):
    ascii_sorted_chars = sorted(s, key=lambda x: ord(x))
    return ascii_sorted_chars[:20]
