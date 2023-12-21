
def remove_repeat_chars(string):
    # Create a new string with the characters of the original string in order
    new_string = ""

    # Iterate over each character in the string
    for char in string:

        # If the current character is not already in the new string
        if char not in new_string:

            # Add the current character to the new string
            new_string += char

        # If the current character is already in the new string
        else:

            # Get the index of the first occurrence of the current character in the new string
            index = new_string.index(char)

            # Remove all occurrences of the current character from the new string after the first occurrence
            new_string = new_string[:index + 1] + new_string[index + 1:]

    # Return the altered string
    return new_string
