
def return_n_smallest_chars(s):
    s_sorted = sorted(s, key=ord)
    s_smallest = s_sorted[:39]
    s_smallest.sort(reverse=True)
    return s_smallest
