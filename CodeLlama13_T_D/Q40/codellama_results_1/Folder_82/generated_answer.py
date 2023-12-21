
def return_n_smallest_chars(s):
    chars = sorted(set(s))
    n = 60
    if len(chars) < n:
        raise ValueError("Number of distinct characters in string must be greater than or equal to the requested number of characters")
    return "".join(chars[:n])
