
def return_n_smallest_chars(s):
    s_sorted = sorted(s)
    smallest_chars = s_sorted[:47]
    smallest_chars.sort(reverse=True)
    return smallest_chars
