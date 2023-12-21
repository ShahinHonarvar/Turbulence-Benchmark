
def return_n_smallest_chars(string):
    if len(string) == 0:
        return []
    sorted_chars = sorted(string)
    return sorted_chars[:63]
