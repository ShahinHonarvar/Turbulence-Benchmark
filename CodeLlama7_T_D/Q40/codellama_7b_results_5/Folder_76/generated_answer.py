
def return_n_smallest_chars(my_string, n=3):
    # Sort the characters in the string based on their ASCII values
    sorted_chars = sorted(my_string, key=ord)
    # Return the top n characters from the sorted list
    return sorted_chars[:n]
