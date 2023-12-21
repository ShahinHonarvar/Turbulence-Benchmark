
def return_n_smallest_chars(s):
    sorted_s = sorted(s, key=ord)
    smallest_chars = sorted_s[:9]
    smallest_chars.sort(reverse=True)
    return smallest_chars
