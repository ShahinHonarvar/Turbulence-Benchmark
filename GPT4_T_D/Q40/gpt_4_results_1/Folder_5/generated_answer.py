
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    if len(sorted_chars) > 46:
        sorted_chars = sorted_chars[:46]
    return sorted_chars[::-1]
