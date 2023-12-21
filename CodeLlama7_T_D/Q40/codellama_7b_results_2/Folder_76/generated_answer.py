
def return_n_smallest_chars(s, n):
    # Sort the characters in the string by their ASCII values
    sorted_chars = sorted(s, key=ord)
    # Return the first 3 characters of the sorted list
    return sorted_chars[:3]
