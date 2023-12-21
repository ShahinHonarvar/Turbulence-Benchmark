
def return_n_smallest_chars(in_string):
    chars_sorted_asc = sorted(in_string, key=ord)
    return chars_sorted_asc[:80]
