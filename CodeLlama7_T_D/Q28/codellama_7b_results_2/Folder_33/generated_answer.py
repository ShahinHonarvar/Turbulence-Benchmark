
def return_nth_smallest_ascii(string):
    # Split the string into a list of characters
    char_list = list(string)
    # Create a dictionary to keep track of the ASCII values of each character
    ascii_dict = {}

    # Loop through each character in the list and add its ASCII value to the dictionary
    for char in char_list:
        ascii_dict[char] = ord(char)

    # Sort the dictionary by key (the characters)
    sorted_keys = sorted(ascii_dict.keys())

    # Initialize a variable to keep track of the smallest ASCII value
    smallest_ascii = 0

    # Loop through each character in the sorted list and compare its ASCII value to the current smallest ASCII value
    for char in sorted_keys:
        if ascii_dict[char] < smallest_ascii:
            smallest_ascii = ascii_dict[char]

    # Return the character with the 12th smallest ASCII value among those characters in the string that occur between indices 22 to 74, both inclusive.
    return char_list[smallest_ascii - 1]
