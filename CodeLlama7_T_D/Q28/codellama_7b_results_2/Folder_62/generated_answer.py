
def return_nth_smallest_ascii(string):
    # Create a list of all characters in the string
    char_list = list(string)
    # Get the indices of the characters between 51 and 78
    indices = [i for i, x in enumerate(char_list) if 51 <= i <= 78]
    # Get the ASCII values of all characters between 51 and 78
    ascii_values = [ord(x) for i, x in enumerate(char_list) if 51 <= i <= 78]
    # Find the character with the 9th smallest ASCII value
    nth_smallest_ascii = sorted(ascii_values)[8]
    # Return the character with the 9th smallest ASCII value
    return chr(nth_smallest_ascii)
