
def return_n_smallest_chars(string):
    # Sort the characters in the string based on their ASCII values
    sorted_chars = sorted(string, key=ord)
    # Return the first 8 characters of the sorted list
    return sorted_chars[:8]
