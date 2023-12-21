
def return_n_smallest_chars(my_string):
    # Create a list of tuples containing the ASCII value and the character
    char_list = [(ord(char), char) for char in my_string]
    # Sort the list by the ASCII value
    char_list.sort()
    # Return the first 58 characters of the sorted list
    return [char for (_, char) in char_list[:58]]
