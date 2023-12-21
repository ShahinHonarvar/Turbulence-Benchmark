
def return_n_smallest_chars(string, n=2):
    # Sort the characters in ascending order based on their ASCII values
    sorted_chars = sorted(string, key=ord)
    # Return the first n characters of the sorted list
    return sorted_chars[:n]
