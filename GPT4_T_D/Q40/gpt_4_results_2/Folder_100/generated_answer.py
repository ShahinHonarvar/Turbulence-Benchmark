
def return_n_smallest_chars(s):
    ascii_list_sorted = sorted(s, key=ord)
    smallest_chars = ascii_list_sorted[:72]
    smallest_chars.sort(reverse=True)
    return smallest_chars
