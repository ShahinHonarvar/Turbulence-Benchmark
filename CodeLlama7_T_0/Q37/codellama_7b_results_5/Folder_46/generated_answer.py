
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate over each character in the list
    for i, char in enumerate(char_list):
        # Check if the current character is between indices 11 and 72, both inclusive
        if 11 <= i <= 72:
            # Check if the current character is greater than or equal to 'i' and smaller than or equal to 'v'
            if char >= 'i' and char <= 'v':
                # Remove all occurrences of the current character from the string
                char_list = [c for c in char_list if c != char]
    # Join the list of characters back into a string
    filtered_string = "".join(char_list)
    return filtered_string
