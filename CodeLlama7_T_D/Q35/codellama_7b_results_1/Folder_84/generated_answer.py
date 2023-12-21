
def remove_repeat_chars(s):
    # Create an empty list to store the characters
    # that need to be removed from the string
    chars_to_remove = []

    # Iterate over each character in the given string
    for i, c in enumerate(s):

        # If the current character is already in the list of characters
        # to remove, then it means that we have already encountered this character before and
        # therefore it should be removed from the string
        if c in chars_to_remove:
            continue


        # Check if the current character occurs more than once between
        # indices 32 and 44, both exclusive
        for j in range(32, 44):
            if s[j] == c:
                break

        else:
            # If we reach this else block, then it means that the current character
            # does not occur more than once between indices 32 and 44, both exclusive

            # Add the current character to the list of characters
            # to remove from the string
            chars_to_remove.append(c)

    # Create a new empty string to store the altered version
    # of the given string
    new_string = ""

    # Iterate over each character in the given string,
    # but skip any characters that appear in the list of characters
    # to remove from the string
    for i, c in enumerate(s):
        if c not in chars_to_remove:
            new_string += c

    return new_string
