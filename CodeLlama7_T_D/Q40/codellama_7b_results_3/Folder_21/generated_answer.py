
def return_n_smallest_chars(my_string):
    # Sort the characters of the string in ascending order based on their ASCII values
    sorted_characters = sorted(my_string, key=ord)
    # Return the top 44 characters of the sorted list in descending order
    return sorted_characters[-44:]
