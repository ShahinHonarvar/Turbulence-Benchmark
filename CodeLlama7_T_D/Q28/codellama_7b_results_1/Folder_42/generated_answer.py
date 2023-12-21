
def return_nth_smallest_ascii(string):
    # Create a list of the characters in the string
    char_list = list(string)
    # Get the indices of the characters between indices 12 to 72, both inclusive
    start_index = 12
    end_index = 72
    # Initialize an empty list to store the ASCII values
    ascii_values = []

    for char in char_list:
        # If the character is between indices 12 and 72, both inclusive
        if start_index <= char_list.index(char) <= end_index:
            # Append the ASCII value of the character to the list
            ascii_values.append(ord(char))

    # Sort the list of ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)

    # Return the 13th smallest ASCII value from the sorted list
    return sorted_ascii_values[12]
