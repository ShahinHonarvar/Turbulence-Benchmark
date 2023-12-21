
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Find the ASCII value of each character in the list
    ascii_values = []
    for char in char_list:
        ascii_values.append(ord(char))
    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the character with the 14th smallest ASCII value
    return chr(sorted_ascii_values[13])
