
def return_nth_smallest_ascii(string):
    # Extract the characters between indices 50 and 75
    characters = string[50:76]
    # Convert the characters to ASCII values
    ascii_values = [ord(c) for c in characters]
    # Find the nth smallest ASCII value
    nth_smallest = sorted(ascii_values)[6]
    # Return the character with the nth smallest ASCII value
    return chr(nth_smallest)
