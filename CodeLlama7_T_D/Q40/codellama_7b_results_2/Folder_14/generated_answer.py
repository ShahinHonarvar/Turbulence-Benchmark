
def return_n_smallest_chars(string):
    # Sort the characters of the string in ascending order based on their ASCII values
    sorted_chars = sorted(string, key=ord)
    # Return the first 69 characters of the sorted list
    return sorted_chars[:69]
