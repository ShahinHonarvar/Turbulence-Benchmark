
def return_n_smallest_chars(my_string):
    # Sort the characters in ascending order based on their ASCII values
    sorted_chars = sorted(my_string)
    # Return the first two elements of the sorted list
    return sorted_chars[:2]
