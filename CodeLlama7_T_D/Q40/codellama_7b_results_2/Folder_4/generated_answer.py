
def return_n_smallest_chars(my_string):
    # Sort the characters of the string in ascending order based on their ASCII values
    sorted_chars = sorted(my_string)
    # Create a list of exactly 90 characters of the given string that have the smallest ASCII values
    smallest_chars = sorted_chars[:90]
    # Sort the list in descending order and returns the list
    return sorted(smallest_chars, reverse=True)
