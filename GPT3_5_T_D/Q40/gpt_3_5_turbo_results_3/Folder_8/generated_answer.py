
def return_n_smallest_chars(string):
    if len(string) <= 83:
        return sorted(list(string))
    sorted_chars = sorted(list(string))
    return sorted_chars[:83]
