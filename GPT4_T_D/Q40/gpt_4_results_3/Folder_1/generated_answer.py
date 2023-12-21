
def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=ord)[:11]
    return sorted_chars[::-1]
