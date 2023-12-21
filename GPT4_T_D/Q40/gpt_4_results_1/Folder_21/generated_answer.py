
def return_n_smallest_chars(s):
    if len(s) < 44:
        raise ValueError('Input string should contain at least 44 distinct characters.')
    sorted_s = sorted(s, key=ord)
    return sorted_s[:44][::-1]
