
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Get the indices of the characters between 22 and 74
    indices = [i for i, x in enumerate(char_list) if 22 <= i <= 74]
    # Create a dictionary to store the ASCII values of the characters
    ascii_dict = {}
    # Loop through the indices and get the ASCII value of each character
    for index in indices:
        char = char_list[index]
        ascii_value = ord(char)
        ascii_dict[char] = ascii_value
    # Sort the dictionary by the ASCII values of the characters
    sorted_dict = sorted(ascii_dict.items(), key=lambda x: x[1])
    # Get the 12th smallest ASCII value from the sorted dictionary
    smallest_ascii_value = sorted_dict[11][1]
    # Return the character with the smallest ASCII value
    return chr(smallest_ascii_value)
