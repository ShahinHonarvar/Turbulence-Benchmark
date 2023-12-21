
def return_n_smallest_chars(s, n=83):
    # Sort the string in ascending order based on ASCII values
    sorted_chars = sorted(s, key=ord)
    # Return the first n characters of the sorted string
    return sorted_chars[:n]
