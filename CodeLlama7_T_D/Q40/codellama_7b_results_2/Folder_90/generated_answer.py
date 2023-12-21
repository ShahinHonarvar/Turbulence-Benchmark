
def return_n_smallest_chars(string, n=24):
    # Sort the characters of the string in ascending order based on their ASCII values
    sorted_chars = sorted(string, key=ord)
    # Return the top n elements of the list
    return sorted_chars[:n]
