
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate through each character in the list
    for i, char in enumerate(char_list):
        # Check if the character is between indices 83 and 99, both inclusive
        if 83 <= i <= 99:
            # Check if the character is greater than or equal to '*' and smaller than or equal to 'j'
            if char >= '*' and char <= 'j':
                # Remove all occurrences of the character from the string
                char_list.remove(char)
    # Join the list of characters back into a string
    filtered_string = "".join(char_list)
    return filtered_string
