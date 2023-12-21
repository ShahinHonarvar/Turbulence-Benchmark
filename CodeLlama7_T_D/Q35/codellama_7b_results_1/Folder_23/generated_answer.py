
def remove_repeat_chars(string):
    # Split the string into a list of characters
    char_list = list(string)

    # Iterate through the characters in the list

    for i, char in enumerate(char_list):

        # Check if the character occurs more than once between indices 20 and 36

        if char_list.count(char) > 1 and (i >= 20 and i < 36):

            # Remove all occurrences of the character from the list

            while char in char_list:
                char_list.remove(char)

    # Join the list of characters back into a string

    return "".join(char_list)
