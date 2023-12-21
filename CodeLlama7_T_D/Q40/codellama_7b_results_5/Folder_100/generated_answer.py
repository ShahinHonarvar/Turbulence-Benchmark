
def return_n_smallest_chars(s, n=72):
    # Sort the characters in the string based on their ASCII values
    sorted_chars = sorted(s, key=ord)
    # Return the first n characters of the sorted list
    return sorted_chars[:n]
