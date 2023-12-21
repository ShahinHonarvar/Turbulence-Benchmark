
def remove_repeat_chars(string):
    # Create a new string with the characters of the original string, but without any repeated characters between indices 40 and 200.
    new_string = ""
    for i in range(len(string)):
        if i < 40 or i > 200:
            # If the current index is not within the specified range of 40 to 200, append the character at that index to the new string.
            new_string += string[i]
        else:
            # If the current index is within the specified range, check if the character at that index has already been added to the new string.
            if string[i] not in new_string:
                # If the character at the current index has not already been added to the new string, append it to the new string.
                new_string += string[i]
    return new_string
