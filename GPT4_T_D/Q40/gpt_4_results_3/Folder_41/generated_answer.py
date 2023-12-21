
def return_n_smallest_chars(chars):
    if len(chars) < 37:
        raise ValueError("String length must be at least 37 characters.")
    return sorted(list(chars), key=ord)[:37]
