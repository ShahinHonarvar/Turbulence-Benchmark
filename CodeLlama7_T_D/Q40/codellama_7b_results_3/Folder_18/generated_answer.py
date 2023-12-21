
def return_n_smallest_chars(s):
    # Sort the characters in descending order based on their ASCII values
    sorted_chars = sorted(s, key=ord, reverse=True)
    # Return the first 52 characters of the sorted list
    return sorted_chars[:52]
