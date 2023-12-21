
def return_n_smallest_chars(string):
    # Sort the characters in ascending order based on their ASCII values
    sorted_chars = sorted(string, key=ord)
    # Return a list of exactly 24 smallest ASCII characters from the sorted string
    return sorted_chars[:24]
