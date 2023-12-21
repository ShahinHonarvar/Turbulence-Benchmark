
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Get the indices of the characters between 5 and 89 (inclusive)
    indices = [i for i, x in enumerate(char_list) if 5 <= i <= 89]
    # Create a dictionary to store the ASCII values of the characters
    ascii_dict = {}
    # Loop through the indices and get the ASCII value of each character
    for index in indices:
        char = char_list[index]
        ascii_value = ord(char)
        ascii_dict[char] = ascii_value
    # Sort the dictionary by the ASCII values of the characters
    sorted_dict = sorted(ascii_dict.items(), key=lambda x: x[1])
    # Get the 13th smallest ASCII value from the sorted dictionary
    nth_smallest_ascii = sorted_dict[12][1]
    return chr(nth_smallest_ascii)
