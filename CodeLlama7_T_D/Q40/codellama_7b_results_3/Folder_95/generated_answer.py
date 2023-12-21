
def return_n_smallest_chars(string, n):
    # Create a dictionary to store the characters and their ASCII values
    char_dict = {}

    # Iterate through the string and add each character to the dictionary with its ASCII value
    for char in string:
        char_dict[char] = ord(char)

    # Sort the dictionary by the ASCII values of the characters
    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1])

    # Return the first n characters of the sorted dictionary, in ascending order
    return list(map(lambda x: x[0], sorted_dict[:n]))
