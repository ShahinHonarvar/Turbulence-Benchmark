
def return_n_smallest_chars(my_string):
    # Sort the characters of the string based on their ASCII values
    sorted_list = sorted(my_string)
    # Return the first 10 characters of the sorted list
    return sorted_list[:10]
