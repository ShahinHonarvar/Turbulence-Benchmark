
def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_chars = sorted_chars[:88]
    smallest_chars = smallest_chars[::-1]
    return smallest_chars
