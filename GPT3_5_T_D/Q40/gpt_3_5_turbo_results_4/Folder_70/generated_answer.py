
def return_n_smallest_chars(chars):
    smallest_chars = sorted(chars)[:2]
    smallest_chars.sort(reverse=True)
    return smallest_chars
