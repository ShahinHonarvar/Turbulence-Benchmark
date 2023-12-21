
def filter_chars(s):
    # Create a list of characters in the string
    chars = list(s)
    # Iterate over the characters in the string
    for i, char in enumerate(chars):
        # Check if the character is between 55 and 84 (exclusive)
        if 55 < ord(char) < 84:
            # Remove all occurrences of this character from the string
            chars = [c for c in s if c != char]
    # Return the altered string
    return ''.join(chars)
