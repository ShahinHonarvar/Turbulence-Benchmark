
def return_nth_smallest_ascii(string):
    # Create a list of unique characters in the string
    char_list = set(string)
    # Initialize a dictionary to store the ASCII values of each character
    ascii_dict = {}
    # Iterate over the list of unique characters and assign their corresponding ASCII values
    for char in char_list:
        ascii_dict[char] = ord(char)
    # Sort the dictionary by value (ASCII value)
    sorted_ascii_dict = dict(sorted(ascii_dict.items(), key=lambda x: x[1]))
    # Return the 10th smallest ASCII value
    return list(sorted_ascii_dict.values())[9]
