
def return_nth_smallest_ascii(s):
    # Find the characters in the string that occur between indices 17 and 86, both inclusive
    chars = set(s[17:86])
    # Create a list of tuples of the form (ASCII value, character) for each character in the string
    ascii_chars = [(ord(c), c) for c in s if c in chars]
    # Sort the list by the ASCII values
    sorted_ascii_chars = sorted(ascii_chars, key=lambda x: x[0])
    # Return the character with the 15th smallest ASCII value
    return sorted_ascii_chars[14][1]
