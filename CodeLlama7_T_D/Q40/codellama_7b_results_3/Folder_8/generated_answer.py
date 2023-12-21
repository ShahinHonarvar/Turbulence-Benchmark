
def return_n_smallest_chars(s, n):
    # Sort the string in ascending order
    s = sorted(s)
    # Return the first n characters of the sorted string
    return s[:n]
