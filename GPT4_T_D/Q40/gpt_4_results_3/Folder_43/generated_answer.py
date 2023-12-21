
def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=ord)[:56]
    sorted_chars.reverse()
    return sorted_chars
