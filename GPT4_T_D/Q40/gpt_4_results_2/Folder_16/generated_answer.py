
def return_n_smallest_chars(string):
    sorted_string = sorted(string, key=ord)[:64]
    sorted_string.sort(reverse=True)
    return sorted_string
