
def return_n_smallest_chars(my_string):
    # Sort the characters in the string based on their ASCII values
    sorted_characters = sorted(my_string)
    # Create a list of exactly 14 characters of the sorted characters
    smallest_characters = sorted_characters[:14]
    # Return the list of smallest characters in ascending order
    return smallest_characters
