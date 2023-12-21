
def return_n_smallest_chars(s):
    # Sort the characters in the string based on their ASCII values
    sorted_chars = sorted(s, key=ord)
    # Return the first 26 characters of the sorted list
    return sorted_chars[:26]
