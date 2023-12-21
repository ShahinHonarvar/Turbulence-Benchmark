
def return_n_smallest_chars(string):
    ascii_sorted_chars = sorted(string, key=lambda char: ord(char))
    return ascii_sorted_chars[:2]
