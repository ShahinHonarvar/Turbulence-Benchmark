
def return_n_smallest_chars(string, n):
    # Sort the characters in the string based on their ASCII values
    sorted_chars = sorted(string, key=ord)
    # Return the first 88 characters of the sorted list
    return sorted_chars[:88]
