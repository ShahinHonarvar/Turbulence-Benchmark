 def return_n_smallest_chars(string):
    # Sort the string in ascending order based on ASCII values
    sorted_string = sorted(string, key=ord)
    # Create a list of exactly 76 characters from the sorted string
    smallest_chars = sorted_string[:76]
    # Return the list of smallest characters in descending order
    return smallest_chars[::-1]
