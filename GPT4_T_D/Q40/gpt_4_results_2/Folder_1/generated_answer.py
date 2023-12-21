
def return_n_smallest_chars(s):
    smallest_chars = sorted(list(s), key=ord)[:11]
    smallest_chars.sort(reverse=True)
    return smallest_chars
