
def return_n_smallest_chars(string, n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    # Sort the characters of the string in descending order based on their ASCII values
    sorted_chars = sorted(string, key=ord, reverse=True)
    # Return the first n characters of the sorted list
    return sorted_chars[:n]
