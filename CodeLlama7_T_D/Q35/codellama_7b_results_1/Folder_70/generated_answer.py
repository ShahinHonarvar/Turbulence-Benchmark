
def remove_repeat_chars(string):
    # create a new string with the removed characters
    new_string = ""

    # loop through each character in the given string
    for char in string:
        # if the current character is not already in the new string
        if char not in new_string:
            # add the character to the new string
            new_string += char

    return new_string
