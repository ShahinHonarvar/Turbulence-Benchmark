
def return_nth_smallest_ascii(string):
    # Get the characters between indices 5 and 89 (inclusive)
    chars = string[5:89]
    # Get the ASCII values of all the characters in the string
    ascii_values = [ord(char) for char in chars]
    # Find the smallest ASCII value among all the characters in the string that occur between indices 5 to 89 (inclusive)
    smallest_ascii_value = min(ascii_values)
    # Get the character with the smallest ASCII value
    smallest_character = chars[ascii_values.index(smallest_ascii_value)]
    return smallest_character
