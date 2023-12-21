
def remove_repeat_chars(string):
    # Create a new string that is the same length as the original string
    new_string = ""

    # Iterate through each character in the original string
    for char in string:

        # If the current character is not already in the new string, append it to the new string
        if char not in new_string:
            new_string += char

        # If the current character is already in the new string, remove all occurrences of that character from the new string
        else:
            new_string = new_string.replace(char, "")

    return new_string
