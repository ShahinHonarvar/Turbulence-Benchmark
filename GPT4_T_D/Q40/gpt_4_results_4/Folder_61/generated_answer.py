
def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s), key=ord)
    if len(sorted_chars) > 66:
        sorted_chars = sorted_chars[:66]
    sorted_chars.sort(reverse=True)
    return sorted_chars
