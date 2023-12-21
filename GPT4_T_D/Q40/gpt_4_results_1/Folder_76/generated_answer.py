
def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_chars = sorted_chars[:3]
    smallest_chars.reverse()
    return smallest_chars
