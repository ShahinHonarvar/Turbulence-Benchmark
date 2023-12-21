
def return_n_smallest_chars(str_):
    min_chars = sorted(str_, key=ord)[:85]
    min_chars.sort(reverse=True)
    return min_chars
