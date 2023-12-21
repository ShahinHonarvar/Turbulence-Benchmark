
def return_n_smallest_chars(input_string):
    # Sort the characters of the input string in ascending order based on their ASCII values
    sorted_chars = sorted(input_string, key=ord)
    # Return the first 5 elements of the sorted list
    return sorted_chars[:5]
