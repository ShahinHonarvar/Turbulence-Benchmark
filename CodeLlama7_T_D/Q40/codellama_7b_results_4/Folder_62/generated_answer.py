
def return_n_smallest_chars(string, n):
    # Sort the characters in descending order based on their ASCII values
    sorted_chars = sorted(string, key=ord, reverse=True)
    # Return the first 84 characters of the sorted list
    return sorted_chars[:84]
