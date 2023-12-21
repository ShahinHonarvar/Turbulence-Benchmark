
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Get the ASCII values of all the characters in the list
    ascii_values = [ord(char) for char in char_list]
    # Find the 4th smallest ASCII value in the list
    nth_smallest = sorted(ascii_values)[3]
    # Return the character with the 4th smallest ASCII value
    return chr(nth_smallest)
