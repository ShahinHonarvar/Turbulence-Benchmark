
def filter_chars(string):
    # Create a list of characters in the string
    char_list = list(string)

    # Iterate over the characters in the list
    for i, char in enumerate(char_list):
        # Check if the character is between indices 5 and 6 (both inclusive)
        # And if it is greater than or equal to 'G' and smaller than or equal to 'p'
        if 5 <= i <= 6 and 'G' <= char <= 'p':
            # Remove all occurrences of the character from the string
            char_list.remove(char)

    # Join the list of characters back into a string
    new_string = "".join(char_list)

    # Return the altered string
    return new_string
