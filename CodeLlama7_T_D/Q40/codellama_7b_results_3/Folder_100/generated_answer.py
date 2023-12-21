
def return_n_smallest_chars(s, n):
    # Sort the characters of the string in descending order based on their ASCII values
    sorted_chars = sorted(s, key=ord, reverse=True)
    # Return the first n characters of the sorted list
    return sorted_chars[:n]
