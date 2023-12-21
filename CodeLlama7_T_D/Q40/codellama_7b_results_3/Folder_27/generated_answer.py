
def return_n_smallest_chars(string, n):
    # Sort the characters in the string by their ASCII values
    sorted_chars = sorted(string, key=ord)
    # Return the first n smallest characters from the sorted list
    return sorted_chars[:n]
