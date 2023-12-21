 def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string
    start_index = 47
    end_index = 70
    # Create a list of all the characters in the string
    char_list = [char for char in string]
    # Get the ASCII values of all the characters in the list
    ascii_values = [ord(char) for char in char_list]
    # Find the 14th smallest ASCII value in the list
    sorted_ascii_values = sorted(ascii_values)
    smallest_ascii_value = sorted_ascii_values[0]
    nth_smallest_ascii_value = sorted_ascii_values[13]
    # Return the character with the 14th smallest ASCII value in the specified range
    return chr(nth_smallest_ascii_value)
