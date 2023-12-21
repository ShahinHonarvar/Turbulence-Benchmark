
def remove_repeat_chars(string):
    # Initialize an empty string to store the altered string
    new_string = ""

    # Iterate through each character in the given string
    for char in string:

        # Check if the current character occurs more than once between indices 32 and 99, both exclusive
        if string.count(char) > 1 and (len(string) - 1 >= 32 and len(string) - 1 <= 99)):

            # If so, remove all occurrences of the current character from the string
            new_string = new_string + char * (string.count(char) - 1)

        # Otherwise, append the current character to the altered string
        else:
            new_string = new_string + char

    # Return the altered string
    return new_string
