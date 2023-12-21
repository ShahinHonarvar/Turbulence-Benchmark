
def return_nth_smallest_ascii(string):
    # Create a list of unique characters in the string
    unique_chars = set(string)
    # Create a dictionary to store the ASCII values of each character
    ascii_values = {}
    # Iterate through each character in the string
    for char in unique_chars:
        # Get the ASCII value of the character
        ascii_value = ord(char)
        # Add the ASCII value to the dictionary
        ascii_values[char] = ascii_value
    # Sort the dictionary by key (character)
    sorted_dict = sorted(ascii_values.items(), key=lambda x: x[1])
    # Get the 4th smallest ASCII value from the sorted dictionary
    fourth_smallest_ascii = sorted_dict[3][1]
    return chr(fourth_smallest_ascii)
