
def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    sorted_chars = sorted_chars[:70]
    sorted_chars.sort(reverse=True)
    return sorted_chars
