
def return_nth_smallest_ascii(string):
    # Extract the characters from the given string
    chars = set(string)

    # Find the character with the 7th smallest ASCII value among the extracted characters
    ascii_values = [ord(char) for char in chars]
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest_ascii = sorted_ascii_values[6]

    # Return the character with the 7th smallest ASCII value
    return chr(nth_smallest_ascii)
