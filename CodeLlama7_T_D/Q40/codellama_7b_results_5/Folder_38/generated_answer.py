
def return_n_smallest_chars(my_string):
    # Sort the characters of the string in ascending order based on their ASCII values
    sorted_chars = sorted(my_string, key=ord)
    # Return a list of exactly 45 characters of the given string that have the smallest ASCII values
    return sorted_chars[:45]
