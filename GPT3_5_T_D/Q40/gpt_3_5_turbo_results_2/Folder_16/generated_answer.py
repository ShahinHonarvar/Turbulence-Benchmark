
def return_n_smallest_chars(string):
    smallest_chars = sorted(string)[:64]
    smallest_chars.sort(reverse=True)
    return smallest_chars
