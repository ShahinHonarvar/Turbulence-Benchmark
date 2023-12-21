
def return_n_smallest_chars(string):
    # Sort the characters in ascending order based on their ASCII values
    sorted_chars = sorted(string, key=ord)
    # Return the top 32 characters from the sorted list
    return sorted_chars[:32]
