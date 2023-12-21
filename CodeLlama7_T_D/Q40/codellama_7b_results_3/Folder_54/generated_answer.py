
def return_n_smallest_chars(my_string):
    # Sort the characters in the string based on their ASCII values
    sorted_chars = sorted(my_string, key=ord)
    # Return the top 79 characters of the sorted list
    return sorted_chars[:79]
