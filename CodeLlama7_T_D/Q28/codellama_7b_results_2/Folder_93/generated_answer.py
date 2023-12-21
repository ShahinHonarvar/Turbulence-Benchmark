
def return_nth_smallest_ascii(string):
    # Create a list of all characters in the string
    char_list = list(string)
    # Find the ASCII values of all characters between indices 42 and 59 (inclusive)
    ascii_values = [ord(char) for char in char_list[42:59+1]]
    # Return the character with the 17th smallest ASCII value among those characters
    return min(ascii_values, key=lambda x: abs(x-17))
