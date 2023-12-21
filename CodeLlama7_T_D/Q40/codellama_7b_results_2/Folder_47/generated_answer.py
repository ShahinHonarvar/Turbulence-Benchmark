
def return_n_smallest_chars(string, n=21):
    # Create a dictionary with the character and its ASCII value
    char_ascii = {}
    for char in string:
        if char not in char_ascii:
            char_ascii[char] = ord(char)

    # Sort the dictionary by the ASCII values of the characters
    sorted_char_ascii = sorted(char_ascii.items(), key=lambda x: x[1])

    # Return the list of smallest ASCII values
    return [char for char, ascii in sorted_char_ascii[:n]]
