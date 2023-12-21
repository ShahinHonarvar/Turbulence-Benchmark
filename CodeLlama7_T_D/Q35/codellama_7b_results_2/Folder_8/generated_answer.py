
def remove_repeat_chars(s):
    # Initialize a new string with the same length as the input string
    new_string = ""

    # Iterate over the characters in the input string
    for char in s:

        # If the character is not already present in the new string, append it to the end of the new string
        if char not in new_string:
            new_string += char

    return new_string
