
def return_n_smallest_chars(s):
    smallest_chars = sorted(s, key=ord)[:43]
    smallest_chars.sort(reverse=True)
    return smallest_chars
