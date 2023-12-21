
def return_n_smallest_chars(chars):
    if len(chars) <= 36:
        return sorted(chars)
    else:
        return sorted(chars)[:36]
