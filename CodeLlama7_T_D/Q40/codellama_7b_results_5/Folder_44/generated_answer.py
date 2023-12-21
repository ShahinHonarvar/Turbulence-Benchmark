
def return_n_smallest_chars(my_string, n):
    # Sort the characters of the string in ascending order based on their ASCII values
    sorted_chars = sorted(my_string, key=ord)
    # Return the first n elements of the sorted list
    return sorted_chars[:n]
