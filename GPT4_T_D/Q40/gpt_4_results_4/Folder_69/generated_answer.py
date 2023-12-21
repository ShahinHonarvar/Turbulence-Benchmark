
def return_n_smallest_chars(s):
    s = sorted(s)
    smallest_chars = s[:65]
    smallest_chars.sort(reverse=True)
    return smallest_chars
