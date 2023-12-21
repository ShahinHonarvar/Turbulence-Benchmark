
def return_n_smallest_chars(s):
    s = sorted(s, key=ord)
    smallest_chars = s[:39]
    smallest_chars.sort(reverse=True)
    return smallest_chars
