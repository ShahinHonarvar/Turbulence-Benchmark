
def return_nth_smallest_ascii(string):
    # Create a list of the characters in the string
    char_list = list(string)
    # Create a dictionary to keep track of the ASCII values of each character
    ascii_dict = {}
    # Loop through the characters in the string and update the ASCII value for each character in the dictionary
    for char in char_list:
        if char not in ascii_dict:
            ascii_dict[char] = ord(char)
    # Sort the dictionary by the ASCII values of the characters
    sorted_ascii_dict = sorted(ascii_dict.items(), key=lambda x: x[1])
    # Return the character with the 11th smallest ASCII value among those characters in the string that occur between indices 25 to 45, both inclusive.
    return sorted_ascii_dict[10][0]
