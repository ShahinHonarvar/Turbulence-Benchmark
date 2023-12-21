
def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=ord)
    if len(sorted_chars) > 47:
        sorted_chars = sorted_chars[:47]
    return sorted_chars[::-1]
