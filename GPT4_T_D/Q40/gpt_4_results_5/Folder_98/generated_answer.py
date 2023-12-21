
def return_n_smallest_chars(s):
    chars_in_asc_order = sorted(s, key=lambda x: ord(x))
    smallest_68_chars = chars_in_asc_order[:68]
    return smallest_68_chars[::-1]
