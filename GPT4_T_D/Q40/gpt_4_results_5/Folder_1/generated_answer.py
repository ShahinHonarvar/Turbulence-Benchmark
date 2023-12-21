
def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=ord)
    smallest_chars = sorted_chars[:11]
    smallest_chars.sort(reverse=True)
    return smallest_chars
