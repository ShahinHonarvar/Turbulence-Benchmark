
def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=ord)
    if len(sorted_chars) < 88:
        return []
    return sorted_chars[:88][::-1]
