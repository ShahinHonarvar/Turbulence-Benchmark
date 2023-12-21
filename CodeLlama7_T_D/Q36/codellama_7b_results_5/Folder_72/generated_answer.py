
def filter_chars(string):
    # Create a list of characters in the string
    char_list = list(string)
    # Loop through each character in the list
    for i, char in enumerate(char_list):
        # Check if the character is between 44 and 68 (both exclusive)
        if 44 < ord(char) < 68:
            # Remove all occurrences of the character from the list
            char_list = [c for c in char_list if c != char]
    return "".join(char_list)
