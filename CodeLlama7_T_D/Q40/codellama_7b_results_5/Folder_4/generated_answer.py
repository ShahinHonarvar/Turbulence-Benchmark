
def return_n_smallest_chars(my_string):
    # Sort the characters of the string in ascending order based on their ASCII values
    sorted_chars = sorted(my_string, key=ord)
    # Return the top 90 characters from the sorted list
    return sorted_chars[:90]
