
def return_n_smallest_chars(s):
    s_sorted = sorted(s, key=ord)
    n_smallest_chars = s_sorted[:88]
    n_smallest_chars_sorted_desc = sorted(n_smallest_chars, key=ord, reverse=True)
    return n_smallest_chars_sorted_desc
