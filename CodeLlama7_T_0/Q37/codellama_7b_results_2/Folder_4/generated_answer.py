
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate over each character in the list
    for i, char in enumerate(char_list):
        # Check if the current character is between indices 19 and 33, both inclusive
        if 19 <= i <= 33:
            # Check if the current character is greater than or equal to 'S' and smaller than or equal to '{', both inclusive
            if char >= 'S' and char <= '{':
                # Remove all occurrences of the current character from the string
                char_list = [c for c in char_list if c != char]
    # Join the list of characters back into a string
    filtered_string = "".join(char_list)
    return filtered_string
